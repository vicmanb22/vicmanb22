# Runway Analysis

Personas: Agency/Consultant/Firm, Equity Investor (VC/PE), Founder/CFO, Private Debt
Use Cases: FDD, FP&A
Task Note: Will

# Q&A

## **How financially healthy is the portfolio company?**

*I want to understand the company's cash position and capital needs without reaching out to the founder.*

VM's platform provides real-time runway analysis and burn rate tracking to investors at any point in time, with automated alerts on critical cash milestones and capital planning insights.

- How much runway does the company have left?
    - The platform syncs directly with accounting software and bank statements to automatically calculate net burn and derive cash runway in months. Trends in cash consumption are instantly available, ensuring investors don't miss critical inflection points hidden in manual reporting or delayed month-end closes.
- What happens if assumptions change?
    - Simulate upside, base, and downside cases by modeling revenue delays, cost overruns, hiring plans, or aggressive expansion strategies. Our platform assists in stress-testing assumptions, providing audit-traceable insights to evaluate capital raise timing, debt drawdowns, or cost optimization needs with confidence.
- When should the company raise its next funding round?
    - The system automatically blends real-time actuals with strategic forecasts to project runway with institutional-grade accuracy. Forecasted revenues, hiring, and OPEX scaling tie into adjusted runway projections, enabling precise determination of when refinancing or fundraising will be required, with clear data to support board discussions and investment decisions.
- Is the company's burn rate trending in the right direction?
    - The platform automatically monitors month-over-month burn rate changes and compares them against forecasted targets. Investors receive monthly updates and can access current burn trends instantly through the platform, enabling proactive conversations before small issues become critical problems.

# V1

*Tagline: From Cash Management to Strategic Advantage*

---

### Live Cashflow Visibility

*Make critical decisions with an up-to-the-minute view of your cash flow.*

Our platform syncs directly with Accounting Software APIs to provide a **live and accurate view** of your cash balance and burn rate. Stop waiting for month-end closes to make critical decisions; get the real-time clarity needed to operate with confidence and efficiency.

---

### Dynamic Scenario Modeling

*Stress-test your assumptions and instantly model any financial forecasts.*

Go beyond static reports by modeling the impact of strategic decisions, from cost-saving initiatives to revenue shifts, on your runway. Our proprietary LLM also assists in **stress-testing assumptions and scenarios**, providing instant insights that transform your forecast into a powerful decision-making tool.

---

### Automated Forecasting

*Know your true runway and plan your next capital raise proactively.*

Our system automatically **blends real-time actuals with your strategic forecasts** to project runway with institutional-grade accuracy. This automated foresight allows you to plan capital raises proactively and providing better alignment with investors and board members from a data-driven POV.

---

## Reference

### **Automated Burn Rate & Liquidity Tracking**

*Real-time visibility into cash position and survival horizon*

Direct integration with journals and bank statements calculates net burn and instantly derives cash runway in months. AI flags trends in cash consumption, ensuring investors and CFOs don’t miss inflection points hidden in manual reporting.

---

### **Forward-Looking Runway Forecasting**

*Project capital needs under different growth and cost strategies*

Our engine ties forecasted revenues, hiring, and OPEX scaling into adjusted runway projections. Investors can simulate upside, base, and downside cases, gaining precision on how long current funding lasts and when refinancing or fundraising will be required.

---

### **Scenario Stress-Tests for Capital Planning**

*Prepare for downturns and protect deal value*

AI-assisted scenarios model shocks such as revenue delays, cost overruns, or aggressive expansion. This empowers founders and investors to align on capital raise timing, debt drawdowns, or cost optimizations with confidence, backed by audit-traceable data.

---

### Sample Terminal Chatbot Q&A

**Prompt:** Analyze the Journal.csv provided then conduct runway analysis for the most recent period on when will the company will run out of cash by calculating the burn rate

### AI Result

I can see you've uploaded the HelixCRM Journal data. Let me analyze this financial information and conduct a runway analysis to determine when the company will run out of cash.

*Using tool: get_table_info...* ✓

*Exploring journal structure and date range...* ✗

*Exploring journal structure and date range...* ✓

*Examining account categories and recent periods...* ✓

*Identifying cash and bank accounts for runway analysis...* ✓

*Calculating monthly cash flow trends for the last 12 months...* ✓

*Calculating total current cash position across all bank accounts...* ✓

*Analyzing burn rate trend over last 6 months for runway calculation...* ✓

## 📊 HelixCRM Financial Analysis & Cash Runway Assessment

**📂 Data Overview:**

- **File:** 20250826_HelixCRM_Journal.csv (4.74 MB)
- **Period:** November 2022 to July 2025 (54,798 journal entries)
- **Total Cash Balance:** $8,236,393.33 (as of July 31, 2025)

### 💰 Current Cash Position by Bank Account

| Bank Account | Balance | Last Transaction |
| --- | --- | --- |
| US Bank | $7,113,891.98 | 2025-07-31 |
| Silicon Valley Bank | $783,595.62 | 2025-07-30 |
| Wells Fargo | $258,941.73 | 2025-07-30 |
| Stripe | $79,060.04 | 2025-07-31 |
| Cash | $903.96 | 2025-07-31 |
| **Total Cash** | **$8,236,393.33** |  |

### 📈 Monthly Cash Flow Analysis (Last 12 Months)

| Period | Revenue | Expenses | Net Cash Flow | Status |
| --- | --- | --- | --- | --- |
| 2025-07 | $449,000.81 | $716,095.26 | **-$267,094.45** | 🔴 Burn |
| 2025-06 | $295,648.36 | $512,474.06 | **-$216,825.70** | 🔴 Burn |
| 2025-05 | $610,866.39 | $880,407.42 | **-$269,541.03** | 🔴 Burn |
| 2025-04 | $1,051,294.63 | $603,793.27 | **+$447,501.36** | 🟢 Positive |
| 2025-03 | $1,072,505.33 | $662,225.16 | **+$410,280.17** | 🟢 Positive |
| 2025-02 | $590,069.79 | $831,353.49 | **-$241,283.70** | 🔴 Burn |
| 2025-01 | $540,323.08 | $644,967.55 | **-$104,644.47** | 🔴 Burn |
| 2024-12 | $415,486.92 | $576,362.75 | **-$160,875.83** | 🔴 Burn |
| 2024-11 | $341,342.75 | $496,378.07 | **-$155,035.32** | 🔴 Burn |
| 2024-10 | $476,286.79 | $548,286.02 | **-$71,999.23** | 🔴 Burn |
| 2024-09 | $389,327.06 | $499,867.08 | **-$110,540.02** | 🔴 Burn |
| 2024-08 | $370,233.26 | $459,229.54 | **-$88,996.28** | 🔴 Burn |

### 🔥 Burn Rate Analysis & Cash Runway

**Recent Burn Pattern (Last 6 Months):**

| Period | Monthly Burn | Trend |
| --- | --- | --- |
| 2025-07 | $267,094.45 | ⚠️ High |
| 2025-06 | $216,825.70 | 📈 Moderate |
| 2025-05 | $269,541.03 | ⚠️ High |
| 2025-04 | $0.00 | ✅ Profitable |
| 2025-03 | $0.00 | ✅ Profitable |
| 2025-02 | $241,283.70 | ⚠️ High |

**💡 Key Burn Rate Calculations:**

- **Last 3 Months Average Burn:** $251,153.73/month
- **6-Month Average Burn (including profitable months):** $199,124.38/month
- **Recent Trend (May-July 2025):** $251,153.73/month

### ⏰ **CASH RUNWAY PROJECTIONS**

Based on current cash position of **$8,236,393.33**:

| Scenario | Monthly Burn Rate | **Runway (Months)** | **Cash Depletion Date** |
| --- | --- | --- | --- |
| **Recent 3-Month Trend** | $251,153.73 | **32.8 months** | **April 2028** |
| **Conservative (6-Month Avg)** | $199,124.38 | **41.4 months** | **January 2029** |
| **Worst Case (May 2025)** | $269,541.03 | **30.6 months** | **February 2028** |

### 🚨 **Critical Findings:**

1. **⚠️ Recent Deterioration:** After 2 profitable months (March-April 2025), the company has burned cash for 3 consecutive months (May-July 2025)
2. **📉 Revenue Volatility:** Monthly revenue ranges from $295K to $1.07M, indicating inconsistent sales performance
3. **💸 High Expense Base:** Monthly expenses consistently above $500K, with July 2025 reaching $716K
4. **✅ Strong Cash Position:** $8.24M provides substantial runway even at current burn rates
5. **🎯 Breakeven Threshold:** Company needs ~$650K+ monthly revenue to cover current expense levels

### 📋 **Recommendations:**

1. **Immediate Actions:**
    - Focus on revenue generation to return to March-April 2025 performance levels
    - Review July 2025 expense spike ($716K vs $603K average)
    - Implement monthly cash flow monitoring
2. **Strategic Planning:**
    - Target monthly revenue of $700K+ for sustainable profitability
    - Consider expense optimization if revenue doesn't recover
    - Maintain 24+ month runway as safety threshold

**Bottom Line:** With current burn rates, HelixCRM has **30-33 months of runway**, providing adequate time for strategic adjustments and growth initiatives.