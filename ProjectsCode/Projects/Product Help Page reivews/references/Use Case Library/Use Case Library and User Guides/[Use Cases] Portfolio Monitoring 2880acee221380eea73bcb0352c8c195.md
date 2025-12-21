# [Use Cases] Portfolio Monitoring

# V2 Structure:

**Portfolio Monitoring Features**

- Auto Data
    - Connect with accounting & bank API
        - Auto-process financial data
        - Accurate data from the source
    - AI-powered Data Room
        - Document upload and consolidation
        - Document identification and categorization of documents
        - File sharing and file access management
- Instant Models
    - Generate instant Institutional-standard Financial Models
        - Auto-gathers document data as input
        - Populate data automatically in VM’s models
        - Auto model creation flow that updates key inputs from Auto Data
        - Built based on IFRS principle
        - Provide key information relevant to Use Case without needing additional calculation
        - Alters on key events (low runway, big sales growth)
        - Performance and debt covenant insights at any point in time
- Performance Notification
    - Automated monthly performance notifications of portcos
    - Provide key information of portcos’ performance metrics and covenant metrics monthly
        - Financial Performance: Revenue, Gross Margin, OPEX, Net Income
        - Financial Health: Cash Balance, Runway
        - Debt Covenant: Liquidity Ratio, Leverage Ratio, Debt Service Coverage Ratio, Fixed-Charge Coverage Ratio
- LLM Chatbot
    - LLM designed for financial analysis: higher accuracy + knowledge in early stage investments financials
    - Answer your time consuming questions
    
    | Feature | Type | Situation/Story (When) | Questions asked by [Persona] | Ideal Situation/How VM would add Value |
    | --- | --- | --- | --- | --- |
    | Auto Data | Data Collection | Your fund is managing 15+ portfolio companies, and each month your team spends days chasing founders for updated financials via email. Companies send data in different formats (PDFs, Excel, screenshots), requiring manual consolidation and reformatting before you can even begin analysis, creating delays in understanding portfolio health. | - What is the current cash balance across all portfolio companies?
    - Why are the financials in different currencies?
    - Why are the account items different in their financial statements and board deck? | - VM's platform connects directly with accounting software via API, automatically pulling financial data from the source and eliminating manual chasing and consolidation.
    - Standardized data extraction ensures consistent formatting across all portfolio companies, providing immediate visibility into portfolio health. |
    | Auto Data | Document Management | Your portfolio companies send board decks, financial reports, and operational updates through various channels (email and shared folders). Critical documents get buried in email threads, and your team spends time searching for the latest version of a financial statement or searching through folders to find relevant documents. | - What are the key talking points in the latest board deck?
    - Does everyone in the team have access to the same updated documents?
    - Have all portfolio companies submitted their latest financials? | - VM's data room centralizes all documents with automatic categorization, eliminating searches through email threads and folders.
    - Version control and permissions ensure your team always accesses the latest documents without coordination overhead. |
    | Instant Models | Model Updates | You want to evaluate portfolio company performance against plan and identify trends across your investments, but updating financial models for each company requires significant bandwidth. This manual work delays your ability to spot companies that are outperforming or underperforming and need different levels of engagement from you. | - Which portfolio companies are ahead or behind their revenue targets?
    - What are the performance trends across the portfolio this quarter?
    - Based on the forecast, what is the trajectory of gross margin for the next 12 months? | - VM's platform automatically generates institutional-standard financial models with data populated from connected sources, eliminating manual model building and updates for each portfolio company.
    - Real-time model updates enable immediate visibility into performance, allowing you to proceed directly to analysis. |
    | Instant Models | Risk Management | One of your portfolio companies is burning through cash faster than expected, but you discover this weeks after the trend started during a scheduled review. The delayed visibility limits your ability to step in early with operational guidance or help the founder secure financing before the situation becomes critical. | - Which portfolio companies are showing concerning burn rate acceleration?
    - What are the top 3 expenses that is causing the increase in monthly cash burn?
    - How many months of runway remain if the current burn rate continues? | - VM's models automatically calculate key risk metrics like burn rate, runway, and cash position, providing immediate visibility into each portfolio company's financial health.
    - Real-time access to these metrics enables you to identify concerning trends early and step in proactively with operational guidance or help secure financing before situations become critical. |
    | Performance Notification | Portfolio Visibility | Your fund consistently monitors the portfolio companies to ensure they stay on track, but this requires multiple repetitive steps each time - gathering new financials from each company, calculating key metrics, analyzing trends, and comparing performance. These manual processes make regular portfolio monitoring time-consuming and difficult to sustain across all your investments. | - What is the company’s runway based on last month’s cash balance and burn rate?
    - How does last month's revenue compare to the month prior across all portfolio companies?
    - Which companies had significant changes in gross margin this quarter? | - VM's platform automatically delivers monthly performance notifications with key metrics like revenue, gross margin, cash balance, and runway across all portfolio companies, eliminating repetitive manual calculations.
    - Standardized reporting enables consistent monitoring without gathering and consolidating data each time, making regular portfolio oversight sustainable. |
    | Performance Notification | Covenant Compliance | Your fund extended debt financing to multiple portfolio companies and needs to ensure borrowers remain solvent and can generate sufficient cash to service debt obligations. Manually tracking covenant compliance and financial health metrics across your portfolio means you're often checking reactively during scheduled reviews, limiting your ability to identify struggling borrowers early and step in with operational guidance before covenant breaches occur. | - What is the current debt service coverage ratio?
    - How leveraged is this company currently compared to the previous month?
    - Which companies are trending toward potential covenant breaches?
    
     | - VM's platform automatically delivers monthly covenant compliance metrics including liquidity ratio, leverage ratio, and debt service coverage ratio for all portfolio companies, eliminating manual tracking.
    - Continuous visibility into covenant health enables you to identify struggling borrowers early and provide operational guidance before covenant breaches occur. |
    | LLM Chatbot | Ad-hoc Analysis | You need to quickly analyze a portfolio company's latest financial performance and position to assess whether they can meet their debt obligations based on their current growth trajectory. Getting these insights requires complex analysis across multiple data points that isn't immediately available, delaying critical decisions about whether to provide additional support or adjust terms. | - Based on current revenue trajectory, can they service their debt obligations?
    - What's the projected debt service coverage ratio if revenue growth continues at the current rate?
    - How does their current cash generation compare to their debt payment schedule? | - VM's LLM Chatbot provides instant, accurate answers to complex financial questions about debt service capacity and growth trajectories, pulling data directly from connected sources.
    - Ask questions in the chat box and receive immediate analysis, enabling timely decisions about providing additional support or adjusting loan terms. |
    | LLM Chatbot | Document Intelligence | You need to understand how a portfolio company's customer concentration or burn rate has evolved over time to inform your next board discussion or assess whether additional support is needed. Manually reviewing past board decks and financials to extract these trends takes time away from higher-value strategic work with your founders. | - How has this company’s top customer revenue concentration changed over the past 12 months?
    - What does the burn rate trend look like over the last 6 quarters?
    - How has the customer acquisition cost trended for the last 12 months? | - VM's LLM Chatbot instantly extracts and analyzes historical trends from documents, answering questions about customer concentration, burn rates, and key metrics without manual review.
    - Immediate access to document insights allows you to prepare for board discussions quickly, freeing time for strategic work with founders. |
    | All Features | Portfolio Support | Your private credit fund manages 20+ portfolio companies and needs to monitor their financial health monthly to ensure borrowers can service their debt obligations and identify which companies need operational support. Your team faces recurring challenges: chasing portfolio companies for updated financials, ensuring reporting deadlines are met, manually updating models, and calculating health metrics - all while providing external support to the founders and trying to focus on sourcing new investment opportunities. | - Which portfolio companies submitted their financials and which are still pending?
    
    - Are borrowers maintaining sufficient debt service coverage to meet their obligations?
    
    - Which companies show deteriorating financial health or at risk of solvency?
    
    - Is the company growing at the pace that could pay us back? | - VM’s platform automatically pulls monthly financials via accounting software API and delivers monthly performance notifications with key health metrics like cash position, debt service coverage, and covenant compliance for companies connected with our platform, eliminating manual data gathering and calculation work.
    
    - VM’s platform auto-populate financial data and generate institutional-standard financial models in minutes for deeper analysis and forecasting in minutes.
    
    - LLM Chatbot provides instant answers to comparative questions across your portfolio, enabling you to quickly identify which borrowers need support and make informed decisions without repetitive analysis, freeing up your team’s bandwidth significantly. |

---

## V1 Structure

Title question:

**Is my portfolio slipping?**

Title answer:

- Quiet misses turn into boardroom shocks and sleepless nights.
- VM syncs numbers, scans news, and flags swings before they spread.

Question1:

**Is my portco *actually* growing?**

Answer1:

- Decks shout “up” while net retention and cohorts whisper “down.”
- VM normalizes KPIs, tracks cohorts, and verifies true growth signals.

Question2:

**What's the *real* burn rate?**

Answer2:

- Headcount creep and vendor bloat hide cash leaks.
- VM reconciles cash flow, forecasts runway, and alerts on burn drift.

Question3:

**Are they hiding bad news?**

Answer3: 

- You hear after churn spikes or a key exec quits.
- VM scans news, socials, and reviews and pings on negative signals.

Question4:

**Why was I blindsided again?**

Answer4:

- Updates arrive late, scattered, and sanitized before board.
- VM auto-syncs weekly metrics and flags variance the moment it starts.

Question4:

**Quarterly reports a time sink?**

Answer4:

- Chasing PDFs and Excel tabs burns days every quarter.
- VM auto-collects data, standardizes KPIs, and exports board-ready packs.

Call-to-Actions question:

**Ready to monitor your portfolio like never before?**

Call-to-Actions content:

Get comprehensive portfolio insights—from valuation updates and financial diagnostics to market signals and news monitoring—all in one platform. No more chasing founders for updates.

Reference sample website

[monitoring (1).html](%5BUse%20Cases%5D%20Portfolio%20Monitoring/monitoring_(1).html)

# **Will the borrower pay me back?**

Last-minute surprises turn strong loans into sleepless nights.
VM watches covenants 24/7, syncs finances daily, and flags issues before they bite.

---

## **Why always chase financials?**

Manual file processing hunts waste weeks and blind you when timing matters most.

VM auto-syncs from accounting tools and standardizes portco reports on schedule.

## **Missed red flags again?**

Cash burn creeps, AR slips, and you only hear after the cliff.

VM tracks leading signals daily and pings you the moment trends turn.

## **Can we scale efficiently?**

More loans mean more chaos, not more insight, without automation.

VM automates workflows, assigns owners, and keeps every remediation auditable.

---

## Call-to-Actions

### **Ready to proactively manage default risk?**

Get real-time covenant monitoring, forward-looking default forecasts, automated revenue verification for RBF, and comprehensive payment schedules—all in one platform.

- Uncertain Q&A
    
    Question4:
    
    **Can I have a clear schedule of payment dates and repayment amounts?**
    
    Answer4:
    
    Get comprehensive repayment schedules showing every payment date, amount due (principal + interest), outstanding balance, and covenant check dates. Whether fixed monthly payments or revenue-based variable amounts, track everything in one organized dashboard with automated reminders for upcoming payments.