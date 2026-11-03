# Mahim Patel — Portfolio Website Master Blueprint & Prompt Library

This document contains the complete strategy, recruiter psychology enhancements, local hosting guide, and modular copy-paste prompts to build an institutional-grade investment analyst & quant portfolio website for **Mahim Patel**.

---

## PART 1: Strategic Homepage Recommendations (Recruiter Psychology)

Institutional recruiters (buy-side, equity research, hedge funds) spend ~45 seconds on a portfolio. Beyond your background, education, and skills, add these **5 high-impact components** to the Homepage:

1. **"Quick Metrics" Ticker Bar (Above the Fold):**
   * *7 Years Market Immersion* (Age 13 → 20)
   * *2+ NISM Certifications* (Series XV Research Analyst, Series XVI Commodity Derivatives)
   * *Hybrid Profile:* Fundamental Valuation + Quantitative Options Greek Tooling (GEX)
   * *Initiation Coverage:* 2 Comprehensive Initiation Reports (BLS Intl., TMB)
2. **"Recruiter 1-Click Fast Track" (Dossier Box):**
   * Recruiters are impatient. Provide a dedicated box with: `[Download 1-Page Resume PDF]`, `[Best Stock Pitch: BLS Intl.]`, `[View NSE GEX Project]`, `[Connect on LinkedIn]`.
3. **Investment Philosophy in 3 Pillars:**
   * Clearly state how you think about capital allocation (e.g., *Forensic Accounting & Margin of Safety*, *Free Cash Flow Yield & Capital Return*, *Quant Risk / Volatility Awareness*).
4. **Current Reading List / Bookshelf:**
   * Show what you are studying (e.g., Howard Marks' *The Most Important Thing*, Damodaran on Valuation, Seth Klarman's *Margin of Safety*). Fund managers respect voracious readers.
5. **SEBI Compliance & Ethics Disclaimer (Footer):**
   * *"Disclaimer: All analysis, portfolio disclosures, and research reports presented here are strictly for educational and personal archival purposes and do not constitute SEBI-registered investment advice."*
   * *Why:* Shows legal maturity and professional awareness.

---

## PART 2: How to Run & Host It Locally First (On your Mac)

The best tech stack for this is **Vite + Tailwind CSS** (or Next.js). It runs locally in 1 second, costs ₹0, has no server dependencies, and when ready, can be deployed to your custom domain with a single command.

### Quick 3-Step Local Setup:
1. Open your Mac Terminal.
2. Initialize a clean Vite project in this directory:
   ```bash
   cd ~/Downloads/"Portfolio Website"
   npm create vite@latest app -- --template vanilla
   cd app
   npm install -D tailwindcss @tailwindcss/vite
   npm run dev
   ```
3. Open `http://localhost:5173` in your browser. Any edit you make to the code updates instantly.

---

## PART 3: The Modular Prompt Library

Use these individual, copy-paste prompts sequentially to construct the website section by section.

---

### 📋 PROMPT 1: Foundation, Design System & Navigation Architecture
```text
Act as a Principal Frontend Engineer and Institutional Finance Web Designer.
I am building a high-conviction personal portfolio website for Mahim Patel (Age 20), an aspiring Equity Research / Investment Analyst with 7 years of market experience (started at age 13) and a hybrid skill set in Fundamental Equity Research and Quantitative Derivatives (NSE GEX).

Design System Requirements:
- Aesthetic: Modern, high-end institutional terminal (inspired by Bloomberg, Stripe, and modern hedge fund sites). Dark slate/charcoal background (#0F172A / #0B0F19) with subtle gold/emerald accents (#10B981 for positive P&L / #F59E0B for highlights).
- Clean typography with tabular numbers (font-mono for financial metrics).
- Navigation Bar: Sticky header with smooth scrolling tabs:
  1. Overview (Home)
  2. 7-Yr Journey (Origins & Track Record)
  3. Current Portfolio & Watchlist
  4. Research Reports (Initiations & 3-Statement Models)
  5. Quant Projects (NSE GEX)
  6. Certifications
  7. Macro Thesis & Blog
  8. Direct Action Button: [Download Resume (PDF)]

Create the foundational index.html and Tailwind CSS configuration with responsive mobile/desktop navigation, smooth scrolling, and modular section containers ready to be populated.
```

---

### 📋 PROMPT 2: The Homepage (Hero, Bio, Recruiter Dossier & Philosophy)
```text
Act as a Career Strategist for Elite Investment Banking and Equity Research roles.
Create the Homepage / Hero Section for Mahim Patel's portfolio.

Include:
1. Hero Header:
   - Name: Mahim Patel
   - Headline: "Equity Research Analyst & Quantitative Derivatives Enthusiast"
   - Tagline: "7 years of market immersion (Age 13 to 20). Combining forensic fundamental analysis with quantitative options market structure."
2. Key Metrics Bar:
   - 7 Years Active Market Track Record
   - NISM XV (Research Analyst) & NISM XVI (Commodity Derivatives) Certified
   - 2 Full Initiation Reports Published
   - Proprietary NSE Gamma Exposure (GEX) Model Built
3. "Recruiter Fast Track" Card:
   - High-visibility banner with instant action buttons: [Download 1-Page Resume], [Read Flagship Stock Pitch], [View P&L Statement Proofs], [LinkedIn].
4. About & Vision Section:
   - Journey summary: Starting personal investing at age 13, evolving from technical trial-and-error to rigorous financial statement analysis and derivative Greeks.
   - Education & Core Competencies: 3-Statement financial modeling, DCF valuation, options Greek profiling (GEX), Python, Excel/VBA.
   - Long-term view: Dedicated to disciplined, long-term capital compounding and institutional research.
5. Investment Philosophy Pillars:
   - Margin of Safety & Capital Preservation
   - Forensic Accounting & Corporate Governance Focus
   - Derivatives-Informed Risk & Liquidity Profiling
6. Bookshelf / Current Reading Card (e.g., Damodaran, Howard Marks, CFA Level 1).
```

---

### 📋 PROMPT 3: Portfolio Management History & Proofs (Age 13 → 20)
```text
Create the "Portfolio Journey & Historical Track Record" section for Mahim Patel's portfolio.

Requirements:
1. Interactive Timeline (Age 13 to Age 20):
   - Age 13-15: First foray into markets, learning market mechanics, understanding order types and market cycles.
   - Age 16-17 (Class 11th-12th): Systematic study of F&O, primary market IPO mechanics, DRHP analysis, and diverse investment instruments (Debt, G-Secs, ETFs, REITs/InvITs, SGBs), transitioning to fundamental valuation.
   - Age 18-20 (Previous FY & University): Macro market avoidance, capturing commodity cycle momentum (Gold/Silver +₹2.35L), Direct IPO alpha (+₹1.22L), and disciplined crypto stop-loss (-₹25k at $105k BTC) resulting in ₹3.50L net realized gains. Live Zerodha verification (https://console.zerodha.com/verified/32efc750), NISM certifications, initiation research reports, and quantitative GEX models.
2. Proof of Work & Historical Statements Showcase:
   - A grid of downloadable and previewable document cards representing verified account statements, holdings records, and ledger histories.
   - Feature a "Confidentiality & Data Integrity" banner explaining that account client IDs and total absolute capital are masked to maintain privacy, while percentage gains, trade timestamps, and holding durations are fully verifiable.
   - Provide interactive modal previews for:
     a) Early Holdings Statement (2020-2021)
     b) Multi-year Investment Ledger
     c) Verified Broker P&L Performance Report
```

---

### 📋 PROMPT 4: Current Portfolio, Live Positions, Thesis & Watchlist
```text
Build the "Current Portfolio, Active Holdings & Watchlist" section.

Requirements:
1. Portfolio Asset Allocation Overview:
   - Visual breakdown bar: Equity (Large/Mid/Small cap), Cash/Liquid, Hedges.
   - Overall Portfolio Benchmark comparison (e.g., Portfolio IRR / Absolute Return vs. NIFTY 50).
2. Active Holdings Table:
   - Columns: Company Name, Ticker, Sector, Entry Date, Weight (%), Return/P&L (%), Conviction Level (High/Medium), Action: [View Thesis Card].
   - When a row is clicked, expand an accordion or modal showing:
     * Investment Thesis (3 core bull points)
     * Key Risks Monitored
     * Margin of Safety & Target Fair Value
3. "Upcoming Opportunities / Watchlist" Sub-Section:
   - Companies currently being researched before deployment.
   - Cards showing: Company Name, Sector, Catalyst being watched (e.g., quarterly earnings turnaround, margin inflection, regulatory tailwind), Target Entry Price, and Current Status (e.g., "Deep-Dive Valuation Phase" or "Awaiting Margin of Safety").
```

---

### 📋 PROMPT 5: Research Reports & 3-Statement Financial Models
```text
Build the "Equity Research Reports & Valuation Models" section.

This is the most critical section for equity research and buy-side internship recruiters.

Requirements:
1. Filter Tabs: [All Reports] | [Initiation Coverage] | [Sectoral / Thematic] | [Financial Models]
2. Featured Research Cards:
   - Report 1: BLS International Initiation Coverage
     * Target Price, CMP, Rating: Buy / Hold
     * 3-Sentence Thesis Summary (Moat, visa outsourcing tailwinds, asset-light scalability)
     * Buttons: [Preview PDF directly on site], [Download Full Research Report], [View Financial Model]
   - Report 2: Tamilnad Mercantile Bank (TMB) Initiation Coverage
     * Key metrics: NIMs, Asset Quality (GNPA/NNPA), Valuation discount relative to peers
     * Buttons: [Preview PDF], [Download Full Report]
3. Financial Modeling Showcase:
   - Highlight of 3-statement dynamic models (P&L, Balance Sheet, Cash Flow linked to DCF and Sensitivity Tables).
   - Card for interactive download of Excel workbooks.
4. Embedded PDF Modal:
   - Allow recruiters to view the full PDF reports directly inside a clean, full-screen responsive reader modal without leaving the website.
```

---

### 📋 PROMPT 6: Quantitative Projects (NSE GEX & Backtesting)
```text
Build the "Quantitative Research & Engineering Projects" section.

Focus on: **NSE GEX (Gamma Exposure) Engine & Weekly Backtest**.

Requirements:
1. Project Hero Card:
   - Title: NSE Options Gamma Exposure (GEX) & Volatility Surface Profiler
   - Tech Stack: Python, Pandas, NSEpy/Option Chain API, Plotly, Streamlit/Matplotlib
   - Problem Statement: Traditional technical analysis ignores options dealer positioning. GEX models dealer hedging dynamics to anticipate market support/resistance and volatility pin levels on weekly expiry days.
2. Architecture & Methodology:
   - Calculation of aggregate Gamma Exposure across Strike Prices.
   - Spot-to-Zero Gamma Level (Transition between mean-reverting and high-volatility regimes).
3. Backtest Report & Performance (1-Week Analysis):
   - Key findings: Pinning accuracy around major GEX nodes during expiry.
   - Clean charts/graphs showing predicted support/resistance levels vs. actual spot price trajectories.
   - Downloadable PDF / Markdown link: [Read 1-Week GEX Backtest Report].
   - Code Repository Link: [View GitHub Repo].
```

---

### 📋 PROMPT 7: Certifications & Continuous Learning Ledger
```text
Build a modular "Certifications & Professional Credentials" section.

Requirements:
1. Dynamic Card Grid that is easy to update with new credentials:
   - Card 1: NISM-Series-XV: Research Analyst Certification Examination
     * Issuing Authority: National Institute of Securities Markets (SEBI Mandated)
     * Core Competencies: Fundamental Analysis, Economic Analysis, Company Valuation, Regulatory Ethics
     * Status: Certified / Active
     * Button: [Verify Certificate / View Credential PDF]
   - Card 2: NISM-Series-XVI: Commodity Derivatives Certification
     * Issuing Authority: NISM
     * Focus: Commodity Market Structure, Hedging & Derivatives Pricing
     * Status: Certified / Active
     * Button: [View Certificate]
   - Card 3: CFA® Program Candidate (Level 1)
     * Focus: Financial Reporting, Equity Investments, Fixed Income, Ethics
     * Status: In Progress / Registered
2. Add a clean placeholder card: "+ Next Goal: [Targeting CFA Level 1 / Financial Modeling Accreditation]" to show continuous growth.
```

---

### 📋 PROMPT 8: Macro Thesis, Blog & SEBI Disclaimer
```text
Build the "Macro Perspectives & Personal Investment Journal" blog section.

Requirements:
1. Blog Card Grid:
   - Clean article preview cards with: Publication Date, Reading Time, Category Tag (Macro, Equity Thesis, Psychology).
   - Sample Articles:
     * "The Anatomy of a Multibagger: Lessons from 7 Years of Microcap Investing"
     * "Demystifying Options Market Structure: Why Gamma Moves Spot"
     * "Evaluating Banking Valuations in an Elevating Credit Cost Cycle"
2. Clean Reader View:
   - Formatted in readable typography with blockquotes, callout boxes, and KaTeX-style math/formula support.
3. Professional Legal & SEBI Disclaimer Footer:
   - Clear institutional disclaimer clarifying that all posts, research, and portfolio holdings are personal intellectual journals and academic research, not investment advice.
   - Contact Bar: Email, LinkedIn, GitHub, and a [Download Dossier] button.
```

---

## PART 4: Roadmap from Localhost to Your Custom Domain

```
Phase 1: Local Development (Now)
  └── Run Vite/Tailwind locally on Mac (http://localhost:5173).
  └── Feed the prompts above to build each section.
  └── Link your actual PDF reports (BLS, TMB) and GEX data.

Phase 2: Push to Free GitHub Repository
  └── Create a private or public GitHub repo: `mahim-portfolio`.
  └── Push your code to GitHub.

Phase 3: Connect to Your Domain
  └── Buy `mahimpatel.com` or `mahimpatel.in` on Cloudflare or Porkbun (~₹1,200 for 2 yrs).
  └── Connect the domain to GitHub Pages / Cloudflare Pages in 2 clicks.
  └── Instant free SSL padlock + live worldwide.
```
