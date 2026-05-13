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

COMPETITOR OVERVIEW:
Cirium is OAG's primary competitor in aviation data and analytics, backed by RELX Group. They deliver aviation intelligence spanning flight schedules, fleet data, on-time performance analytics, emissions reporting, and flight status tracking to airlines, airports, and travel companies globally. Cirium serves 900+ airlines with particularly strong market presence in North America through their DIIO Mi analytics platform. Recent innovation focuses on operational use cases, building on their strength in fleet and aircraft data.

OAG COMPETITIVE POSITIONING (shareable with customers):
OAG stands out for its data freshness and platform completeness, processing significantly more schedule updates than Cirium and refreshing data every 15 minutes. OAG is also the only provider able to combine schedules, real-time status, and airline-sourced pricing in a single platform — a capability Cirium cannot replicate. OAG processes 400k+ schedule updates per day (instance view) vs Cirium's 280k (effective view), with 15-minute product refreshes and up to 24 months of forward-looking schedules vs Cirium's 12 months.

WHY OAG IS BETTER THAN CIRIUM:
1. COMPREHENSIVE PRICING INTELLIGENCE: OAG offers the highest quality pricing dataset through Infare's unique give-to-get model. Cirium has no comprehensive pricing proposition — a critical gap for airlines needing integrated schedules + fares.
2. UNIFIED SCHEDULES + STATUS: OAG uniquely combines schedules and status for complete flight lifecycle visibility. Cirium cannot easily join these datasets, creating fragmentation.
3. SUPERIOR DATA FRESHNESS: OAG processes 400k+ daily schedule changes (vs Cirium's 280k) with 15-minute updates and 24-month forward schedules (vs Cirium's 12 months).
4. SIMPLIFIED UNIFIED API: OAG offers a single Flight Info API plus Alerts. Cirium runs fragmented API families (FlightStats/Flex vs Sky) with different auth, SDKs, and docs.
5. GOLD-STANDARD REPUTATION: OAG's 90+ years of heritage and IATA partnership cement our reputation as the industry's most trusted schedules provider.
6. CLOUD-FIRST PLATFORM: Fast onboarding 24-48 hours vs Cirium's 6-8 weeks (Snowflake/AWS onboarding).
7. BROADEST PORTFOLIO: OAG uniquely combines supply, demand, and pricing datasets. No competitor matches this breadth for commercial analysis.

OAG STRENGTHS vs CIRIUM:
- Only provider with schedules + demand + pricing (Cirium has no pricing)
- Unified schedules + status tracking — single view from schedule publish to touchdown (Cirium cannot do this)
- Fast cloud deployment: 24-48 hours vs Cirium's 6-8 weeks
- 1,500+ customers across 10+ verticals

OAG GAPS/WEAKNESSES:
- Status data gaps: Incomplete gate info — departure gate coverage 56% vs Cirium's 69%
- Emissions accuracy: Not audited; behind Cirium's >99% ISAE 3000-certified model
- Analytics UI: Analyser has legacy tech issues; modernisation in progress

CIRIUM STRENGTHS:
- Fleet valuations & aviation finance consultancy — strongest in market
- Strong in NAM airports — DIIO Mi deeply embedded in North America, high switching costs
- Superior gate data coverage (69% vs OAG's 56%)
- 49% share of voice in aviation, finance, ESG and AI data market
- Key partnerships: Aireon (satellite ADS-B), FlightRadar24, Travelport MIDT (exclusive booking data)

CIRIUM WEAKNESSES:
- No pricing data — cannot serve airline revenue management teams; major competitive gap
- Separated schedules & status data — products don't integrate; complex API ecosystem
- Slower cloud evolution — limited cloud platform traction; focus on legacy SSIM/flat files
- 6-8 weeks cloud onboarding vs OAG's 24-48 hours

STATUS DATA BAKE-OFF — OAG vs CIRIUM (39,042 flights, Jan-Feb 2026 independent trial):
OAG beat Cirium in 9 of 11 key metrics:
- 9.3 minutes faster detecting arrival time changes
- 22.2 minutes faster on gate assignments
- 12× more likely to detect runway touchdown first (59% vs 5%)
- 1-2 minutes more accurate on time predictions across all forecast horizons
- 5 distinct flight states vs Cirium's 3 (Cirium doesn't even offer InGate status)
- OAG delivers arrival estimate corrections first 67% of the time
- OAG delivers departure gate information first 67% of the time
- 865 data sources vs Cirium's 600
Where Cirium leads: departure gate coverage 69% vs OAG's 56%

TALK TRACKS — WHY WE WIN:

1. PRICING DATA NEED:
"I understand you're evaluating Cirium. They're strong on the operational side — fleet data, emissions — but when it comes to pricing intelligence, there's really no comparison. Cirium doesn't have a fare data proposition. If you need to understand competitive fares, pricing trends, or do revenue management analysis, you'll need to source that elsewhere. With our Infare acquisition, we give you schedules AND the most comprehensive fare intelligence in the market — all in one place."

2. UNIFIED FLIGHT LIFECYCLE (schedules + status):
"One thing that consistently comes up with Cirium customers is the challenge of joining their schedules and status data. They run separate API families — FlightStats for status, Cirium Sky for schedules — with different authentication, different SDKs, different documentation. It's a real integration headache. With OAG, you get one API, one authentication model, one data structure that covers the entire flight lifecycle. You can track a flight from the moment it's scheduled all the way through to touchdown and gate arrival. We call it 'publish to touchdown' visibility, and Cirium simply can't match that unified experience."

3. CLOUD-NATIVE BUYERS:
"If you're working in a modern data stack with Snowflake or cloud-based analytics, the difference is night and day. Cirium takes 6-8 weeks to onboard. We get you up and running in 24-48 hours. They're still deeply tied to legacy SSIM flat files. We're cloud-native by design. We push 400,000 schedule updates per day, every 15 minutes. Cirium does 280,000 per day. If you're building products or making decisions that need fresh data fast, we're the only real choice."

4. DATA RELIABILITY:
"When we ran a head-to-head comparison on 39,000 flights, OAG was consistently faster and more accurate on the metrics that matter for real-time decisions — detecting flight changes, delivering gate updates, estimating arrival times. It's not that Cirium's data is bad — it's that when milliseconds or minutes matter, OAG has the edge. And for mission-critical applications, that edge is everything."

OVERALL COMPETITIVE RESPONSE:
"While Cirium has legitimate strengths — fleet valuations, aviation finance advisory, strong North America coverage with DIIO Mi, and better gate data coverage — it doesn't tell the full story. In a bake-off of 39,042 flights, OAG beat Cirium in 9 of 11 status metrics — we're 9.3 minutes faster on arrival changes, 22.2 minutes faster on gates, 12× more likely to detect touchdown first. More critically: Cirium has no pricing data, their schedules and status don't integrate, and they're focused on legacy SSIM/flat files. OAG is the only provider offering schedules + demand + pricing unified in one platform, with true schedule-to-touchdown tracking and 24-48 hour cloud deployment versus their 6-8 weeks."

TALK TRACKS — WHY WE LOSE:

STATUS DATA QUALITY CONCERNS:
"While Cirium's gate data coverage may be better than ours, it doesn't tell the full story. We recently ran head-to-head testing, and OAG won 9 out of 11 metrics. We're 12 times faster at detecting landings, we deliver arrival updates 9 minutes faster, and when we do have gate data, we deliver it 22 minutes faster. Our coverage is 56% versus their 69% — so yes, they have more gates. But we have 865 data sources to their 600, and our estimates are 1-2 minutes more accurate across the board. So here's the real question: do you need gate data for 13% more flights, or do you need faster, more accurate status updates for everything else?"

FLEET/VALUATIONS PRIORITY:
"I understand fleet data is a priority for you. You're right that Cirium has built a strong reputation in this area. Here's what I'd encourage you to consider: what percentage of your use cases actually require deep fleet data versus schedule, capacity, and connectivity intelligence? We partner with ch-aviation for fleet data, which covers the core fleet intelligence most commercial teams need. If fleet valuations are absolutely central to your business, Cirium may be the better fit for that specific use case. But if you're making network planning, scheduling, or commercial strategy decisions, our schedule accuracy and coverage will likely drive more value."

ESG/EMISSIONS REPORTING:
"Right now, Cirium is ahead of us in this area with their certified emissions data. That said, where we do excel is in the commercial intelligence that helps you make business decisions about which routes to fly, which markets to enter, and how to optimise your network. Some organisations use OAG for commercial planning and supplement with specialised ESG tools for compliance reporting. Would that kind of approach work for your organisation, or is having everything in one platform non-negotiable?"

NAM AIRPORT ANALYTICS (DIIO Mi):
"DIIO Mi has been the standard for North American airports for years, and switching costs are real. You've got trained staff, historical reports, and workflows built around it. But here's what I'd ask you to consider: what's the cost of staying with the status quo? Are there pain points with your current setup — the user experience, the time to get insights, platform flexibility, or pricing trajectory? What are the biggest limitations you're facing with your current setup?"

PROOF POINTS:
- Air India chose OAG over Cirium for Flight Info Alerts and Schedules Data: "OAG was more accurate than Cirium because when the aircraft departs or arrives, the actual time is updated in OAG's database more accurately."
- Independent trial: OAG detected arrival time changes 9 minutes faster on average
- 47.8% of flights had gate information 30+ minutes earlier from OAG
- Blue Skies Consulting chose OAG over Cirium for Traffic Analyser: "provided the best value for the data they required"
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
