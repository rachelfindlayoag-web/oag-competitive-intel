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

COMPETITOR OVERVIEW:
RateGain is an India-headquartered SaaS provider founded in 2004 serving 3,100+ customers across travel and hospitality in 100+ countries. Publicly traded. Positioned as a broad-based travel tech platform covering hotels, OTAs, airlines, and car rentals. Core strength remains hotel and OTA-centric — airlines are a newer expansion. Their airline product is AirGain, launched 2017.

RATEGAIN PRODUCTS:
- AirGain Rate Intelligence: Real-time airfare pricing intelligence across 200+ airlines, 700+ websites (OTAs, metasearch, brand sites, GDS). Key features: FlightWise (automated O&D tracking), Fare Evolution (historical pricing), Market Sense (automated alerts), AI-Powered Route Digest (Q1 2025 — daily AI executive summary). Claims 98% accuracy and 95% sufficiency SLAs.
- AirGain Parity Watchtower: Monitors fare consistency across distribution channels to prevent revenue leakage. Markets itself as "industry's first parity solution."
- Adara (2022 acquisition): Traveler intent data from loyalty programs and clickstream — forward-looking demand signals similar to 3Victors' DemandView.
- Key RMS integrations: Accelya airRM, Maxamation Aviator RM.
- Built on Google Cloud (BigQuery, Pub/Sub).

OAG COMPETITIVE POSITIONING (shareable with customers):
OAG stands out for its focus on data quality — 86% of pricing data collected directly from airlines through give-to-get partnerships, delivering far greater accuracy than scrape-led models. OAG covers >2x as many websites and airlines vs RateGain (1,500+ websites, 500+ airlines vs RateGain's ~700 websites, ~200 airlines). RateGain relies heavily on web scraping (only 20% direct from airlines), introducing volatility, missing fares, and OTA-biased prices. OAG is airline-native; RateGain's roots and strength remain hotel and OTA-centric.

WHY OAG IS BETTER THAN RATEGAIN:
1. SUPERIOR DATA QUALITY: OAG collects ~86% via give-to-get directly from airlines. RateGain only 20% direct — rest is web-scraped OTA data. OTA data ≠ airline.com pricing.
2. AIRLINE-NATIVE EXPERTISE: OAG is purpose-built for airline revenue management. RateGain's core is hotels — airline veterans question their airline-specific capabilities.
3. UNRIVALLED MARKET COVERAGE: OAG covers >1,500 websites, >500 airlines vs RateGain's ~700 websites, ~200 airlines. More than 2x the coverage.
4. PROVEN ACCURACY: Multiple airlines chose OAG after finding RateGain's data unreliable — Eurowings, Allegiant, Pegasus, Flyadeal specifically returned to OAG after RateGain quality issues.
5. SUPERIOR SUPPORT: Airlines using both platforms consistently report better responsiveness, airline expertise, and problem-solving from OAG vs RateGain.

OAG STRENGTHS:
- 86% airline-direct give-to-get partnerships with contractual G2G agreements
- Unmatched global coverage — >2x websites and airlines vs RateGain
- Trusted market leader — Finnair (10+ years), Ryanair, easyJet, Turkish Airlines are long-term customers
- Airline-native company vs hotel-tech company

OAG GAPS/WEAKNESSES:
- Premium pricing model: OTA/MSE data collection costs significantly higher than RateGain (who bundles it with hotel contracts)
- Complex product suite: Pharos, PPS, Market Trends — overlapping tools create onboarding friction
- Pricing data refresh in hours vs RateGain's "real-time" marketing claim (though no provider has true live data)

RATEGAIN STRENGTHS:
- Claims real-time data shopping (vs batch), 98% accuracy SLA, 95% sufficiency SLA
- User-friendly UI: rapid onboarding 48-72 hours, unlimited custom reports, 24/7 support, 99.5% uptime
- Comprehensive channel coverage: 200+ airlines, 700+ websites, OTA/MSE/GDS/mobile
- AI-Powered Route Digest (Q1 2025) — daily automated AI executive summary, boosted stock price
- Lower cost for OTA/MSE data — bundled through existing hotel contracts
- RMS integrations with Accelya and Maxamation

RATEGAIN WEAKNESSES:
- Only 20% direct airline data — 80% web scraped through QL2 and OTA channels. "Real-time" doesn't address OTA-manipulated pricing.
- Multiple airlines left RateGain citing data quality issues and returned to OAG: Eurowings, Allegiant Air, Flyadeal, Pegasus.
- 24/7 support claim contradicted by airline feedback — OAG consistently rated more responsive and airline-focused.
- Hotel-centric heritage: airline revenue managers question depth of airline expertise.
- Limited airline coverage: ~200 airlines vs OAG's 500+.

OVERALL COMPETITIVE RESPONSE:
"OAG's 86% airline-direct give-to-get model vs RateGain's 20% direct means we deliver actual airline.com pricing, not OTA-displayed prices. Multiple airlines — Eurowings, Allegiant, Pegasus — chose OAG after experiencing RateGain's data quality issues. We cover 1,500+ websites and 500+ airlines, more than double RateGain's coverage. Yes, we're more expensive — because we don't take shortcuts. When you're making million-dollar pricing decisions, do you trust airline-direct data or OTA-displayed prices?"

TALK TRACKS — WHY WE WIN:

1. SUPERIOR DATA QUALITY:
"More than 80% of our data is sourced directly from airlines through contractual agreements — actual airline.com pricing. RateGain only gets 20% direct from airlines and relies on web-scraped OTA data. Multiple airlines have left RateGain and came to us specifically citing data quality concerns with OTA-sourced data. The issue? OTA data doesn't equal airline.com data — it's what OTAs choose to display. When you're making million-dollar pricing decisions, do you trust airline-direct data or OTA-displayed prices?"

2. AIRLINE EXPERTISE AND LONG-TERM PARTNERSHIPS:
"We're recognized as the industry benchmark — airlines trust us with their most critical pricing decisions. Look at Finnair — they've been with us for over 10 years. Ryanair, easyJet, Turkish Airlines — long-term customers who've stayed with us. RateGain is relatively new to airlines — they're known for hotels. When your revenue team needs to defend a pricing strategy to the executive board, do they want to rely on a hotel tech provider trying to break into airlines, or the industry standard that's been trusted for decades?"

3. UNMATCHED GLOBAL COVERAGE:
"We cover 1,500+ websites and 500+ airlines. RateGain covers 700 websites and 200 airlines — less than half. That's blind spots in your competitive intelligence. Network carriers can't afford to miss what competitors are doing on routes we track but they don't."

TALK TRACKS — WHY WE LOSE:

PREMIUM PRICING:
"We're more expensive because we don't take shortcuts. RateGain gets OTA data bundled into their hotel contracts — it's cheap for them. We collect more than 80% of our data directly from airlines through contractual agreements. That costs more, but it's accurate airline.com pricing, not OTA-displayed prices. The question isn't whether we're more expensive — it's whether making million-dollar pricing decisions on cheap, scraped data is worth the risk. Some airlines paid for the cheaper option first, then switched to us or came back after experiencing data quality issues."

WIDER USE CASE / HOLIDAY PACKAGES / GSAs:
"We're laser-focused on airline revenue management — that's our core. RateGain is a multi-vertical travel tech company covering hotels, car rentals, and vacation packages. If you're a holiday package department needing vacation bundle pricing, or a GSA managing multiple small airlines looking for one affordable contract across all your clients, RateGain's broader travel portfolio and lower price point makes sense. We don't try to be everything to everyone — we're built for airlines making strategic pricing decisions."

PRODUCT INNOVATION / UI:
"RateGain excels at rapid feature releases — they launched AI Digest and Market Sense in months and have a modern, intuitive interface that gets analysts productive quickly. We take a different approach. Our products — Pharos, PPS, Market Trends — are comprehensive and battle-tested by airlines like Finnair for over 10 years. More powerful but requires more training time. The trade-off: do you want the latest features fast with a simpler interface, or depth, accuracy, and proven reliability that scales with your network complexity?"

PROOF POINTS:
- Eurowings, Allegiant Air, Flyadeal, Pegasus all returned to OAG after leaving for RateGain citing data quality issues
- Finnair: 10+ year OAG customer — long-term airline loyalty
- RevenueMindz chose RateGain at 2.5x lower price but later admitted "we might not have understood what more was in the package with OAG"
- Airlines using both platforms consistently rate OAG support as more responsive and airline-focused
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

COMPETITOR OVERVIEW:
3Victors is a Virginia-based start-up founded in 2015, acquired by ATPCO in December 2023. They pioneered Travel Data Analytics as a Service, processing billions of flight search data points to provide real-time market insights. Named "AI Company of the Year" in 2024 by TravelTech Breakthrough. Strong US presence with customers including American Airlines and JetBlue. ATPCO aims to achieve 80% dynamic offers by 2026 with 3Victors as a core enabler — however, innovation has notably slowed since acquisition with very limited presence in recent airline pricing RFPs.

3VICTORS PRODUCTS:
- PriceEye: Competitive pricing intelligence. Fuses direct booking queries, GDS shopping data, and web scrapes. Real-time responsiveness. Only ~10% give-to-get vs OAG's 86%.
- DemandView: Demand forecasting. Filters ~60% bot traffic from search data to reveal true consumer intent. Combines search demand, pricing, capacity, and booking data.
Key data partnerships: QL2 for scraped pricing data (acknowledged lower quality than OAG), AWS.

OAG COMPETITIVE POSITIONING (shareable with customers):
OAG stands out for its focus on data quality — 86% of pricing data collected directly from airlines through give-to-get partnerships, delivering 98% data completeness and 98.4% timeliness. 3Victors relies on GDS and scraped data — inferred proxies, not a reflection of actual market prices. OAG also offers broader historical depth (10+ years, 4 trillion historical price points) and uniquely combines schedules and pricing in a single framework.

WHY OAG IS BETTER THAN 3VICTORS:
1. SUPERIOR DATA QUALITY: 86% of OAG pricing data via give-to-get model vs 3Victors' ~10%. 98% completeness and 98.4% timeliness vs web-scraped data quality.
2. COMPREHENSIVE MARKET INTELLIGENCE: OAG offers Supply (schedules) + Demand (bookings) + Pricing + Status. 3Victors offers only search signals and pricing.
3. HISTORICAL DEPTH: 10+ years of historical airfare data with 4 trillion historical price points. 3Victors lacks comparable archives.
4. PROVEN MARKET LEADER: 90+ years, 1,500+ customers across 10+ verticals vs 3Victors' limited brand recognition.
5. POST-ACQUISITION UNCERTAINTY: Innovation has slowed significantly since ATPCO's December 2023 acquisition. No major product launches or new combined offerings materialised. Very limited RFP presence.
6. GLOBAL FOOTPRINT: OAG in 190+ countries, 10 global offices. 3Victors primarily US-centric.

OAG STRENGTHS:
- Broadest datasets: Supply, Demand, Pricing & Status for comprehensive analysis
- Highest quality pricing data: 86% via give-to-get model
- 10+ years historical data, 4 trillion price points
- Established market leader — 90+ years, 1,500+ customers

OAG GAPS/WEAKNESSES:
- Limited real-time AI & demand signals: More traditional delivery (updates in hours) vs 3Victors' real-time search streaming
- Premium pricing model: Higher cost can be barrier for cost-sensitive airlines
- No forward-looking consumer demand data (yet): Lack true consumer search/intent signals like DemandView

3VICTORS STRENGTHS:
- AI-driven real-time technology — filters billions of search queries for clean demand data
- ATPCO backing — access to 90% of airlines via ATPCO relationships
- Named "AI Company of the Year" 2024 — strong innovation narrative
- Real-time streaming of search demand data

3VICTORS WEAKNESSES:
- Poor data quality: ~10% give-to-get, rest is web-scraped (QL2) — lower quality than OAG
- Limited brand recognition: Not widely known; expected to remain embedded tech not sought-after brand
- Post-acquisition stagnation: Very limited innovation, no major product launches since Dec 2023 acquisition
- US-centric: Limited global perspective for international carriers
- No historical depth: Cannot support long-term pricing strategy or seasonality analysis

OVERALL COMPETITIVE RESPONSE:
"We respect 3Victors' AI technology and real-time capabilities, but when selecting a pricing intelligence partner, data quality and proven reliability matter most. 86% of OAG's pricing data comes directly from airlines through our give-to-get model compared to their less than 10% — the rest of their data is web-scraped, which simply cannot match our 98% completeness and 98.4% timeliness. Since ATPCO's acquisition, 3Victors has shown slowed innovation with very limited presence in recent airline pricing RFPs. Beyond data quality, OAG provides the broadest range of datasets in the market — Supply, Demand, Pricing, and Status — giving you comprehensive commercial analysis rather than just search intent signals. The choice comes down to this: innovative technology with uncertain data quality and post-acquisition risk, or the proven, trusted foundation with superior data quality that the world's leading airlines rely on to make confident pricing decisions every day."

TALK TRACKS — WHY WE WIN:

1. SUPERIOR DATA QUALITY (GIVE-TO-GET):
"The fundamental difference is data quality. We source 86% of our pricing data directly from airlines — 3Victors gets only ~10%, with the rest web-scraped through QL2. That's why we deliver 98% completeness and 98.4% timeliness. Yes, they offer real-time search data, but would you rather have minute-by-minute updates of uncertain quality, or rock-solid data you can confidently base your pricing strategy on?"

2. PROVEN STABILITY vs POST-ACQUISITION UNCERTAINTY:
"Let's talk about stability. We've been the trusted aviation data partner for 90+ years with 1,500+ customers. 3Victors? Since ATPCO acquired them in December 2023, innovation has stalled — we're seeing very limited RFP activity from them. When you're presenting your vendor recommendation to leadership, which name carries more weight: OAG, the industry gold standard, or 3Victors, an embedded technology with unclear post-acquisition direction that most airline executives haven't heard of?"

3. COMPREHENSIVE MARKET INTELLIGENCE:
"Search intent is interesting, but it's just one signal. What about actual capacity on the route? What are real booking trends showing? What's the historical pricing pattern? We give you Supply, Demand, Pricing, and Status — the complete market view. 3Victors gives you search signals and scraped pricing. When your revenue manager needs to defend a network decision, do they want to say 'search data shows interest' or 'here's the complete market picture with actual bookings, capacity, and 10+ years of pricing trends'?"

TALK TRACKS — WHY WE LOSE:

REAL-TIME CAPABILITY GAP:
"While 3Victors offers more real-time search data streaming than we do currently, we focus on what matters most for pricing decisions: data quality, historical depth, and comprehensive market context. Our 86% give-to-get model delivers 98% completeness and 98.4% timeliness, plus 10+ years of historical data and complete market view across Supply, Demand, and Pricing. That's the foundation for confident strategic decisions."

PERCEPTION OF INNOVATION:
"While 3Victors won an AI award in June 2024 and has compelling technology messaging, since ATPCO acquired them in December 2023 there have been no major product announcements, no new releases, and very limited presence in recent airline pricing RFPs. Innovation appears to have slowed significantly post-acquisition. Ask them to show you what's actually been released since the acquisition."

ATPCO ECOSYSTEM ADVANTAGE:
"The ATPCO connection is real — if you're already using multiple ATPCO products, the idea of an integrated ecosystem is attractive. What I'd point out is that since the December 2023 acquisition, we haven't seen concrete evidence of that integration materialising. Just make sure you ask them for specific timelines and customer references who've successfully implemented since the acquisition."
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
