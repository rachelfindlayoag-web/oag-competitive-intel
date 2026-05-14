import os
import atexit
import threading
import sqlite3
from datetime import timedelta
from functools import wraps

from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db"))
DASHBOARD_PASSWORD = os.environ.get("DASHBOARD_PASSWORD", "oag-intel-2026").strip()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            company       TEXT NOT NULL,
            title         TEXT NOT NULL,
            url           TEXT,
            summary       TEXT,
            source_type   TEXT,
            category      TEXT DEFAULT 'Press Coverage',
            published_at  TEXT,
            discovered_at TEXT DEFAULT (datetime('now')),
            UNIQUE(company, url, title)
        )
    """)
    try:
        c.execute("ALTER TABLE items ADD COLUMN category TEXT DEFAULT 'Press Coverage'")
    except Exception:
        pass
    c.execute("DELETE FROM items WHERE source_type = 'website_change'")
    conn.commit()
    conn.close()


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "oag-intel-secret-change-in-prod")
    app.permanent_session_lifetime = timedelta(hours=12)
    init_db()

    from scraper import run_all_scrapers

    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(run_all_scrapers, "interval", hours=4, id="scrape_job")
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    threading.Thread(target=run_all_scrapers, daemon=True).start()

    # ── Auth routes ────────────────────────────────────────────────────────────

    @app.route("/login", methods=["GET", "POST"])
    def login():
        error = None
        if request.method == "POST":
            if request.form.get("password", "").strip() == DASHBOARD_PASSWORD:
                session.permanent = True
                session["logged_in"] = True
                return redirect(url_for("dashboard"))
            error = "Incorrect password — please try again."
        return render_template("login.html", error=error)

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))

    # ── Main pages ─────────────────────────────────────────────────────────────

    @app.route("/")
    @login_required
    def dashboard():
        return render_template("index.html")

    @app.route("/playbook")
    @login_required
    def playbook():
        return render_template("playbook.html")

    @app.route("/pitch")
    @login_required
    def pitch():
        from battlecards import OAG_PRODUCTS, BATTLECARDS
        competitors = list(BATTLECARDS.keys())
        return render_template("pitch.html", products=OAG_PRODUCTS, competitors=competitors)

    @app.route("/api/pitch", methods=["POST"])
    @login_required
    def generate_pitch():
        if not GROQ_API_KEY:
            return jsonify({"error": "GROQ_API_KEY not configured. Please add it in Render environment variables."}), 500

        data = request.json or {}
        competitor  = data.get("competitor", "")
        products    = data.get("products", [])
        customer    = data.get("customer", "")
        context     = data.get("context", "")

        from battlecards import BATTLECARDS, OAG_OVERVIEW

        battlecard = BATTLECARDS.get(competitor, "No battlecard available for this competitor.")

        # Pull recent intel items for this competitor from DB
        conn = get_db()
        c = conn.cursor()
        c.execute(
            "SELECT title, summary, category, published_at FROM items WHERE company = ? ORDER BY published_at DESC LIMIT 8",
            (competitor,)
        )
        recent_items = c.fetchall()
        conn.close()

        recent_intel = "\n".join([
            f"- [{row['category']}] {row['title']}: {(row['summary'] or '')[:200]}"
            for row in recent_items
        ]) or "No recent intel available."

        products_str = ", ".join(products) if products else "General OAG data products"

        prompt = f"""You are an expert sales coach at OAG Aviation, the world's leading aviation data company.

A sales rep is preparing for a competitive deal and needs sharp, confident talking points.

=== OAG CONTEXT ===
{OAG_OVERVIEW}

=== COMPETITOR BATTLECARD: {competitor} ===
{battlecard}

=== RECENT INTEL ON {competitor.upper()} ===
{recent_intel}

=== THIS DEAL ===
Customer / Prospect: {customer if customer else 'Not specified'}
Additional context: {context if context else 'None provided'}
OAG Products being pitched: {products_str}
Competitor they are up against: {competitor}

=== YOUR TASK ===
Generate a concise, punchy sales brief for this rep. Structure it as:

**Why OAG wins this deal**
3-4 bullet points on OAG's strongest advantages against {competitor} for the products being pitched.

**Watch out for**
2-3 likely objections the prospect might raise (based on {competitor}'s pitch) and a sharp one-line response to each.

**Recent intel to drop**
1-2 bullet points referencing the most relevant recent {competitor} news the rep can use to show they've done their homework.

**Opening line**
One confident, natural opening line the rep could use to position OAG vs {competitor} in the first 2 minutes of the call.

Keep everything concise, direct and usable in a real sales conversation. No fluff."""

        try:
            import requests as http_req
            resp = http_req.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gemma2-9b-it",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 2048
                },
                timeout=30
            )
            if not resp.ok:
                msg = resp.json().get("error", {}).get("message", resp.text)
                return jsonify({"error": msg}), 500
            result = resp.json()["choices"][0]["message"]["content"]
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # ── API ────────────────────────────────────────────────────────────────────

    @app.route("/api/items")
    @login_required
    def get_items():
        company  = request.args.get("company")
        category = request.args.get("category")

        conn = get_db()
        c = conn.cursor()

        conditions, params = [], []
        if company:
            conditions.append("company = ?")
            params.append(company)
        if category:
            conditions.append("category = ?")
            params.append(category)

        where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        c.execute(
            f"SELECT * FROM items {where} ORDER BY published_at DESC, discovered_at DESC LIMIT 300",
            params,
        )
        items = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(items)

    @app.route("/api/stats")
    @login_required
    def get_stats():
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT company, COUNT(*) as count FROM items GROUP BY company")
        counts = {row["company"]: row["count"] for row in c.fetchall()}
        c.execute("SELECT MAX(discovered_at) as last_updated FROM items")
        row = c.fetchone()
        conn.close()
        return jsonify({"counts": counts, "last_updated": row["last_updated"] if row else None})

    @app.route("/api/refresh", methods=["POST"])
    @login_required
    def trigger_refresh():
        threading.Thread(target=run_all_scrapers, daemon=True).start()
        return jsonify({"status": "ok", "message": "Refresh started in background"})

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
