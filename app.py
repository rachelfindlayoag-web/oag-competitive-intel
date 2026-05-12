import os
import atexit
import threading
import sqlite3

from flask import Flask, render_template, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db"))


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
    # Add category column to existing databases that predate this field
    try:
        c.execute("ALTER TABLE items ADD COLUMN category TEXT DEFAULT 'Press Coverage'")
    except Exception:
        pass
    # Remove old website-change noise from any previous runs
    c.execute("DELETE FROM items WHERE source_type = 'website_change'")
    conn.commit()
    conn.close()


def create_app():
    app = Flask(__name__)
    init_db()

    from scraper import run_all_scrapers

    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(run_all_scrapers, "interval", hours=4, id="scrape_job")
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    threading.Thread(target=run_all_scrapers, daemon=True).start()

    @app.route("/")
    def dashboard():
        return render_template("index.html")

    @app.route("/api/items")
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
    def trigger_refresh():
        threading.Thread(target=run_all_scrapers, daemon=True).start()
        return jsonify({"status": "ok", "message": "Refresh started in background"})

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
