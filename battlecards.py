# Battlecard knowledge base — update these with content from Seismic

OAG_PRODUCTS = [
    "Global Schedules",
    "Flight Status",
    "Seats",
    "Emissions",
    "Master Data",
    "Connections",
    "Minimum Connection Times (MCTs)",
    "Historical Schedules",
    "Historical Status",
    "Passenger Booking Data",
    "Airfare Data",
    "Airfare Market Trends",
    "Airfare Data – Altus",
    "Schedules Analyser",
    "Connections Analyser",
    "Traffic Analyser",
    "Market Trends",
]

OAG_DELIVERY_METHODS = [
    "Data Direct (Snowflake)",
    "API",
    "Alerts",
    "Analytics",
]

BATTLECARDS = {
    "Cirium": """
CIRIUM BATTLECARD

WHO THEY ARE:
Cirium (owned by RELX/LexisNexis) is OAG's closest direct competitor in aviation data. They offer flight schedules, status, analytics and consultancy. Formerly known as FlightGlobal and Flightview. Strong in MRO and airline analytics.

THEIR STRENGTHS:
- Strong brand recognition from FlightGlobal heritage
- Broad consultancy and analytics offering
- Good MRO data
- Sky Suite analytics platform
- Strong relationships with airlines and airports

THEIR WEAKNESSES:
- Schedule data quality lags OAG — OAG is the original source for IATA schedules
- Less granular real-time flight status vs OAG
- Seats data coverage is weaker than OAG
- Higher price point for comparable data
- More complex / slower to integrate
- Support can be slow; large corporate structure
- No direct Snowflake integration as seamless as OAG Data Direct

OAG ADVANTAGES vs CIRIUM:
- OAG is the IATA-designated data aggregator — our schedules are the authoritative source
- OAG Data Direct (Snowflake) delivers data faster and more easily than Cirium's delivery
- OAG Flight Status refreshes up to every 1 minute vs Cirium's less frequent updates
- OAG Seats data is more comprehensive with better predicted seat counts
- OAG has broader historical schedules data (back to 1996 via Schedules Analyser)
- OAG is more agile and easier to work with as a partner
- OAG pricing is more competitive for equivalent coverage

KEY OBJECTIONS & RESPONSES:
- "We already use Cirium": Ask what specific data they use — OAG likely covers it at higher quality or lower cost. Offer a data comparison.
- "Cirium has more analytics tools": OAG Analytics suite (Schedules, Connections, Traffic, Market Trends Analysers) covers the core use cases. And OAG data can plug into any BI tool.
- "Cirium is a bigger company": OAG has been the aviation data authority since 1929 — we're not a startup. IATA chose OAG as the official schedule aggregator.

WIN THEMES:
- Data quality and authority (IATA-designated)
- Speed and freshness of data delivery
- Ease of integration (Snowflake / API)
- Better value for equivalent coverage
""",

    "RateGain": """
RATEGAIN BATTLECARD

WHO THEY ARE:
RateGain is a travel & hospitality technology company focused on revenue management, distribution and marketing AI. They acquired DHISCO and have expanded into airline distribution data. Publicly listed on Indian stock exchange. Primarily a hotel/hospitality tech company that has expanded into aviation.

THEIR STRENGTHS:
- Strong in hospitality / hotel revenue management
- Airfare competitive intelligence tools (AirGain)
- Large distribution network in travel industry
- Growing AI/ML capabilities
- Good partnerships with OTAs and GDSs

THEIR WEAKNESSES:
- Aviation is not their core — hospitality is. Aviation data depth is limited.
- Airfare data coverage is narrower than OAG's
- No flight schedules or status data
- No seats data, no connections, no historical flight operations data
- Primarily a software/SaaS company — not a raw data provider
- Limited global reach vs OAG's truly global coverage

OAG ADVANTAGES vs RATEGAIN:
- OAG is a pure aviation data company — schedules, status, seats, connections are all core products
- OAG has much deeper and more authoritative aviation data than RateGain
- OAG Airfare Altus provides 5+ years historical + 1 year forward airfare data
- OAG Market Trends covers 26 weeks forward airfare from 2015
- For any airline, airport or aviation use case, OAG is purpose-built; RateGain is not
- OAG Data Direct (Snowflake) delivers data at scale that RateGain can't match

KEY OBJECTIONS & RESPONSES:
- "We use RateGain for revenue management": OAG and RateGain can be complementary — OAG for schedule/status/seats data, RateGain for their RM tools. But for raw aviation data, OAG is the authority.
- "RateGain has AI features": OAG data feeds AI models with authoritative input data — without good data, AI output is unreliable.

WIN THEMES:
- Aviation data depth and authority
- Breadth of data products (schedules + status + seats + airfare + historical)
- Pure aviation focus vs hospitality-first competitor
""",

    "Aggregate Intelligence": """
AGGREGATE INTELLIGENCE BATTLECARD

WHO THEY ARE:
Aggregate Intelligence (Aggi) is a niche aviation data company focused on airline schedules and capacity data, primarily serving revenue management and network planning teams. A smaller, specialist competitor.

THEIR STRENGTHS:
- Focused specifically on schedule and capacity intelligence
- Can be agile and responsive as a smaller company
- Competitive pricing on schedule data
- Some customers prefer working with a boutique supplier

THEIR WEAKNESSES:
- Much smaller coverage and data breadth than OAG
- No flight status data
- No real-time data delivery
- No airfare data
- No Snowflake/direct delivery infrastructure
- Limited historical depth
- Fewer analytics tools and no equivalent to OAG's Analyser suite
- Smaller team means limited support and development roadmap
- Less trusted by large enterprise customers who need reliability guarantees

OAG ADVANTAGES vs AGGREGATE INTELLIGENCE:
- OAG is the IATA-designated global schedule aggregator — Aggi sources data that ultimately comes through OAG
- OAG covers flight status, seats, airfare, connections — Aggi does not
- OAG Data Direct (Snowflake) and API infrastructure is enterprise-grade
- OAG has data going back to 1996; Aggi's historical depth is limited
- OAG has global airline relationships and IATA partnerships Aggi cannot match
- Enterprise customers need OAG's reliability SLAs, compliance, and scale

KEY OBJECTIONS & RESPONSES:
- "Aggi is cheaper": Ask what data products they need — OAG likely provides much more for a comparable total cost. Cheaper data with gaps costs more in the long run.
- "Aggi is more responsive/personal": OAG has dedicated account management and a growing customer success function.

WIN THEMES:
- Data authority and IATA relationship
- Breadth of products Aggi simply doesn't offer
- Enterprise reliability and scale
- Long-term data history
""",

    "3Victors": """
3VICTORS BATTLECARD

WHO THEY ARE:
3Victors is an aviation data and analytics company focused on air travel demand forecasting, booking data and passenger intelligence. They focus on helping airlines, airports and travel companies understand passenger demand patterns.

THEIR STRENGTHS:
- Specialised passenger booking and demand data
- Good airline distribution/booking analytics
- Focused product for revenue management teams
- Strong relationships with some US carriers

THEIR WEAKNESSES:
- Narrow focus — primarily booking/demand data
- No schedule data, no flight status, no real-time operations data
- Limited geographic coverage vs OAG's global reach
- Small team, limited product breadth
- No Snowflake delivery or enterprise data infrastructure
- Less established outside of North America

OAG ADVANTAGES vs 3VICTORS:
- OAG Passenger Booking Data covers January 2019 forward with 1 year forward, refreshed weekly/monthly — comparable coverage
- OAG Traffic Analyser provides booking/passenger data within a broader analytics suite
- OAG provides the full picture: schedules + status + seats + bookings + airfare in one place
- OAG's global coverage is unmatched — 3Victors skews US/North American
- OAG Data Direct (Snowflake) delivers booking data alongside all other OAG data products in one pipeline
- OAG has been the aviation data authority since 1929 — enterprise trust and reliability

KEY OBJECTIONS & RESPONSES:
- "3Victors has specialised booking data": OAG Traffic Analyser and Passenger Booking Data covers the core use case. Ask specifically what data points they're missing from OAG.
- "3Victors is our existing supplier": Position OAG as the consolidation opportunity — replace multiple point solutions with one authoritative data partner.

WIN THEMES:
- Full aviation data platform vs narrow point solution
- Global coverage vs North American focus
- Consolidate multiple vendors into OAG
- Enterprise infrastructure and reliability
""",
}

OAG_OVERVIEW = """
OAG COMPANY OVERVIEW:
OAG has been the world's leading aviation data company since 1929. We are the IATA-designated global flight schedules aggregator — the authoritative source for flight schedule data used by airlines, airports, travel companies, governments and technology firms worldwide.

OAG DATA PRODUCTS:
- Global Schedules: 2 years forward, refreshed daily (Direct) / every 15 min (API/Alerts). Back to 1996 via Schedules Analyser.
- Flight Status: 52hr before departure to 48hr after arrival. Near real-time (up to 1 minute) via API and Alerts.
- Seats: Predicted and actual seat counts. -2 to +2 years. Refreshed with schedule and aircraft registration changes.
- Emissions: Flight emissions data from 2019.
- Master Data: Locations, Equipment, Carriers — refreshed daily.
- Connections: 1 year forward, refreshed weekly. Connections Analyser available.
- MCTs (Minimum Connection Times): March 2024 to current, refreshed daily.
- Historical Schedules: From January 2019 (Direct). Back to 1996 (Schedules Analyser).
- Historical Status: From January 2017.
- Passenger Booking Data: January 2019 to 1 year forward. Weekly/monthly refresh. Traffic Analyser available.
- Airfare Data: Live data. Airline PPS, Pharos, Channel Monitor, Retailer PPS analytics.
- Airfare Market Trends: 26 weeks before departure, from 2015. Market Trends Analyser.
- Airfare Data – Altus: 5+ years historical, 1 year forward. Refreshed weekly.

OAG DELIVERY METHODS:
- Data Direct (Snowflake): Direct data delivery into customer's Snowflake environment. No ETL needed.
- API: RESTful API with near real-time data. Up to 1-minute refresh on status.
- Alerts: Push notifications on schedule/status changes.
- Analytics: Web-based analyser tools (Schedules, Connections, Traffic, Market Trends Analysers).

KEY DIFFERENTIATORS:
1. IATA-designated global schedule aggregator — the authoritative source
2. Longest history in aviation data (since 1929)
3. Most comprehensive global coverage — 900+ airlines, 4,000+ airports
4. Data Direct (Snowflake) — easiest enterprise data delivery on the market
5. Full data ecosystem: schedules + status + seats + airfare + bookings in one place
6. Near real-time flight status (up to 1 minute refresh)
"""
