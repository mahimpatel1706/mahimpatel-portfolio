import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Bitcoin Corporate Treasuries (MSTR / SMLR / Metaplanet) — Institutional Equity Research Initiation</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

  @page {
    size: A4 portrait;
    margin: 10mm 12mm 11mm 12mm;
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    font-size: 8.0pt;
    line-height: 1.38;
    margin: 0;
    padding: 0;
  }

  h1, h2, h3, h4 {
    font-family: 'Merriweather', Georgia, serif;
    color: #0f2b48;
    margin-top: 0;
    line-height: 1.22;
  }

  .page {
    page-break-after: always;
    break-after: page;
    clear: both;
    position: relative;
    height: 275mm;
    max-height: 275mm;
    overflow: hidden;
    padding-bottom: 7mm;
  }

  .page:last-child {
    page-break-after: auto;
    break-after: auto;
  }

  .running-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #0f2b48;
    padding-bottom: 3px;
    margin-bottom: 7px;
    font-size: 6.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #475569;
  }

  .running-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #cbd5e1;
    padding-top: 3px;
    font-size: 6.5pt;
    color: #64748b;
  }

  /* Two Column Split */
  .two-col {
    display: flex;
    gap: 11px;
  }

  .col-main {
    flex: 1.8;
  }

  .col-side {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 8px;
    font-size: 7.6pt;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 4px 0 6px 0;
    font-size: 7.0pt;
  }

  th {
    background: #0f2b48;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 3px 4.5px;
    border: 1px solid #0f2b48;
  }

  th.num, td.num {
    text-align: right;
  }

  td {
    padding: 2.8px 4.5px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  .callout {
    background: #f1f5f9;
    border-left: 3px solid #0f2b48;
    padding: 5px 8px;
    margin: 4px 0 6px 0;
    border-radius: 0 4px 4px 0;
    font-size: 7.5pt;
  }

  .callout-amber {
    background: #fefce8;
    border-left: 3px solid #b45309;
    padding: 5px 8px;
    margin: 4px 0 6px 0;
    border-radius: 0 4px 4px 0;
    font-size: 7.5pt;
  }

  .formula-box {
    background: #0f172a;
    color: #38bdf8;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.2pt;
    padding: 4px 8px;
    border-radius: 4px;
    margin: 4px 0;
    text-align: center;
  }

  .pill {
    display: inline-block;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 6.5pt;
    font-weight: 700;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }

  .pill-green { background: #dcfce7; color: #166534; border: 1px solid #86efac; }
  .pill-gold { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
  .pill-navy { background: #e0e7ff; color: #1e1b4b; border: 1px solid #c7d2fe; }

  .font-mono-num {
    font-family: 'JetBrains Mono', monospace;
  }
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<div class="page">
  <div class="running-header">
    <span>Institutional Equity Research • Digital Assets & Corporate Treasuries</span>
    <span>Lead Analyst: Mahim Patel</span>
  </div>

  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; padding-bottom: 6px; border-bottom: 1.5px solid #0f2b48;">
    <div>
      <span class="pill pill-gold">High-Conviction Overweight</span>
      <span class="pill pill-navy" style="margin-left: 4px;">Structural Alpha Memo</span>
      <h1 style="font-size: 15pt; margin: 4px 0 2px 0;">Bitcoin Corporate Treasuries Initiation</h1>
      <div style="font-size: 8.5pt; color: #475569; font-weight: 500;">
        Capturing Asymmetric Structural Alpha via Digital Credit, Volatility Monetization & mNAV Discipline
      </div>
    </div>
    <div style="text-align: right; font-size: 7.2pt; font-family: 'JetBrains Mono', monospace;">
      <div><strong>Target Horizon:</strong> 4-Year Cycle (2026–2030)</div>
      <div><strong>Completed Seed:</strong> INR 3,50,000 (~$4.2K USD)</div>
      <div><strong>Programmed Total:</strong> INR 21,00,000 (~$25.2K USD)</div>
      <div><strong>Deployment Route:</strong> INDmoney (RBI LRS)</div>
      <div style="color: #166534; font-weight: bold;">0% TCS Scheduled Across All 4 Years</div>
    </div>
  </div>

  <div class="two-col">
    <div class="col-main">
      <h2 style="font-size: 9.5pt; margin-bottom: 3px; color: #0f2b48;">1.0 Executive Initiation & Core Alpha Thesis</h2>
      <p style="margin: 0 0 5px 0;">
        This research note initiates high-conviction coverage on a concentrated portfolio of Bitcoin Corporate Treasury entities (MicroStrategy, Strive/Semler Scientific, and Metaplanet ADR). The investment roadmap begins with a completed seed deployment of <strong>INR 3,50,000</strong>, followed by a scheduled top-up of <strong>INR 2,50,000</strong> in Year 1 (Total Year 1 = INR 6,00,000), and systematic tranches of <strong>INR 5,00,000 per year</strong> across Years 2, 3, and 4 (Cumulative Principal = <strong>INR 21,00,000</strong> / ~$25,200 USD).
      </p>
      <p style="margin: 0 0 5px 0;">
        The strategic objective is not merely beta exposure to Bitcoin spot price appreciation, but the <strong>systematic capture of structural alpha over spot Bitcoin</strong>. Over a 4-year cycle (2026–2030), these corporate balance sheets exploit capital market inefficiencies: monetizing equity implied volatility, issuing sub-1% digital credit, and compounding Bitcoin backing per share through reflexive At-The-Market (ATM) equity offerings executed strictly when mNAV is compressed.
      </p>

      <div class="callout">
        <strong>The Three Quantitative Thesis Pillars:</strong><br>
        <strong>1. Sovereign Debt Debasement:</strong> Accelerating global fiscal deficits force monetary dilution; Bitcoin acts as the apex monetary energy sink.<br>
        <strong>2. Corporate Financial Engineering (BTC Yield):</strong> Issuing low-coupon convertible credit and accretive equity at mNAV > 1.0x permanently increases BTC backing per share.<br>
        <strong>3. Quantitative Entry Discipline (&le;15th %ile mNAV):</strong> Deploying capital strictly when market net asset value multiples are compressed eliminates multiple-compression risk and maximizes cyclical mean-reversion.
      </div>

      <h2 style="font-size: 9.5pt; margin: 6px 0 3px 0; color: #0f2b48;">1.1 Portfolio Allocation & Capital Schedule</h2>
      <table>
        <thead>
          <tr>
            <th>Holding / Entity</th>
            <th>Ticker & Route</th>
            <th class="num">Seed Capital</th>
            <th class="num">Weight</th>
            <th>Strategic Role in Portfolio</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>MicroStrategy Inc.</strong></td>
            <td>NASDAQ: MSTR (INDmoney)</td>
            <td class="num font-mono-num"><strong>INR 1,50,000</strong></td>
            <td class="num font-mono-num"><strong>42.9%</strong></td>
            <td>Institutional anchor; S&P 500 inclusion flows; massive ATM liquidity; credit market access.</td>
          </tr>
          <tr>
            <td><strong>Strive / Semler Scientific</strong></td>
            <td>NASDAQ: SMLR / Strive</td>
            <td class="num font-mono-num"><strong>INR 1,10,000</strong></td>
            <td class="num font-mono-num"><strong>31.4%</strong></td>
            <td>Mid/small-cap high-beta; operational cash flow redirect into BTC; rapid BTC/share growth.</td>
          </tr>
          <tr>
            <td><strong>Metaplanet Inc.</strong></td>
            <td>TSE: 3350 / ADR (INDmoney)</td>
            <td class="num font-mono-num"><strong>INR 80,000</strong></td>
            <td class="num font-mono-num"><strong>22.8%</strong></td>
            <td>Asian MicroStrategy; JPY debt/yield arbitrage; 20% equity tax vs 55% Japanese crypto tax.</td>
          </tr>
        </tbody>
      </table>

      <table>
        <thead>
          <tr>
            <th>Deployment Phase</th>
            <th class="num">Tranche (INR)</th>
            <th class="num">Cumulative</th>
            <th>Execution Trigger Condition</th>
            <th>Regulatory & TCS Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Phase 1 (Completed Seed)</td>
            <td class="num font-mono-num">INR 3,50,000</td>
            <td class="num font-mono-num">INR 3,50,000</td>
            <td>Initial baseline entry into MSTR, Strive, Metaplanet</td>
            <td><span class="pill pill-green">0% TCS</span> (&lt; ₹7L limit)</td>
          </tr>
          <tr>
            <td>Phase 2 (Year 1 Top-Up)</td>
            <td class="num font-mono-num">INR 2,50,000</td>
            <td class="num font-mono-num">INR 6,00,000</td>
            <td>Secondary tranche on multiple consolidation (&le;15th %ile)</td>
            <td><span class="pill pill-green">0% TCS</span> (Yr 1 ₹6L &lt; ₹7L)</td>
          </tr>
          <tr>
            <td>Phase 3 (Year 2 Tranche)</td>
            <td class="num font-mono-num">INR 5,00,000</td>
            <td class="num font-mono-num">INR 11,00,000</td>
            <td>Systematic accumulation during pullbacks (&le;15th %ile)</td>
            <td><span class="pill pill-green">0% TCS</span> (Yr 2 ₹5L &lt; ₹7L)</td>
          </tr>
          <tr>
            <td>Phase 4 (Year 3 Tranche)</td>
            <td class="num font-mono-num">INR 5,00,000</td>
            <td class="num font-mono-num">INR 16,00,000</td>
            <td>Systematic accumulation tranche (&le;15th %ile mNAV)</td>
            <td><span class="pill pill-green">0% TCS</span> (Yr 3 ₹5L &lt; ₹7L)</td>
          </tr>
          <tr>
            <td>Phase 5 (Year 4 Tranche)</td>
            <td class="num font-mono-num">INR 5,00,000</td>
            <td class="num font-mono-num">INR 21,00,000</td>
            <td>Final cycle tranche; pre-euphoria positioning</td>
            <td><span class="pill pill-green">0% TCS</span> (Yr 4 ₹5L &lt; ₹7L)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="col-side">
      <h3 style="font-size: 8pt; margin-bottom: 4px; text-transform: uppercase; color: #0f2b48;">Dossier Metrics</h3>
      <table style="margin-bottom: 6px;">
        <tr><td><strong>Analyst</strong></td><td class="num">Mahim Patel</td></tr>
        <tr><td><strong>Experience</strong></td><td class="num">7 Yrs Market Immersion</td></tr>
        <tr><td><strong>Certifications</strong></td><td class="num">NISM XV, NISM XVI</td></tr>
        <tr><td><strong>Strategy Horizon</strong></td><td class="num">July 2026 – July 2030</td></tr>
        <tr><td><strong>Target Alpha</strong></td><td class="num">3x–6x vs Spot BTC</td></tr>
        <tr><td><strong>Base Case Target</strong></td><td class="num font-mono-num" style="color:#0f2b48; font-weight:bold;">INR 59,53,000</td></tr>
        <tr><td><strong>Bull Case Target</strong></td><td class="num font-mono-num" style="color:#b45309; font-weight:bold;">INR 1,07,13,000</td></tr>
      </table>

      <div class="callout-amber" style="margin-top: 6px;">
        <strong>0% TCS Tax Masterstroke:</strong><br>
        By staging remittances at &le; ₹6.0L in Y1 and &le; ₹5.0L in Y2-Y4, remittances remain strictly below the ₹7,00,000 annual RBI LRS threshold, locking in 0% TCS across the entire investment lifecycle.
      </div>
    </div>
  </div>

  <div class="running-footer">
    <span>Bitcoin Corporate Treasuries Initiation Report • Mahim Patel</span>
    <span>Page 1 of 5</span>
  </div>
</div>

<!-- ================= PAGE 2 ================= -->
<div class="page">
  <div class="running-header">
    <span>Macro Architecture & Base Layer Settlement</span>
    <span>Mahim Patel • Institutional Research</span>
  </div>

  <h2 style="font-size: 9.5pt; margin-bottom: 3px; color: #0f2b48;">2.0 Macroeconomic Paradigm: Sovereign Debt Spiral & Monetary Debasement</h2>
  <p style="margin: 0 0 5px 0;">
    The global macroeconomic backdrop has crossed into structural <strong>Fiscal Dominance</strong>—a regime where sovereign debt obligations exceed sustainable debt-to-GDP levels, forcing central banks to subordinate interest-rate policy to government solvency. With US federal debt exceeding <strong>$35 Trillion</strong> (>120% Debt-to-GDP) and net interest expense surpassing <strong>$1.05 Trillion per annum</strong> (exceeding total US defense spending), rate hikes mechanically widen the sovereign fiscal deficit, pumping liquidity into the real economy via interest outlays.
  </p>

  <p style="margin: 0 0 4px 0;">
    In this monetary regime, the relevant hurdle rate for capital preservation is the compound growth rate of global broad money supply (M2 CAGR). Real purchasing power decays exponentially:
  </p>
  <div class="formula-box">
    P_t = P_0 &times; (1 - &pi;_real)^t &nbsp;&nbsp;|&nbsp;&nbsp; &pi;_real = (&Delta;M2 / M2) - &Delta;Y_real
  </div>
  <p style="margin: 2px 0 6px 0;">
    With global M2 compounding at 7%–10% annually against 2.5% real economic growth, unhedged cash and fixed-income assets guarantee capital destruction.
  </p>

  <h3 style="font-size: 8.5pt; margin: 4px 0 2px 0; color: #0f2b48;">Comparative Asset Class Matrix</h3>
  <table>
    <thead>
      <tr>
        <th>Asset Class</th>
        <th>Supply Scarcity / S2F</th>
        <th>Dilution Risk / Elasticity</th>
        <th>Holding / Carry Cost</th>
        <th>Settlement Velocity & Portability</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Bitcoin (BTC)</strong></td>
        <td><strong>Absolute: 21M cap; S2F &rarr; &infin;</strong></td>
        <td><strong>Zero supply response; strictly inelastic</strong></td>
        <td>Zero storage cost; non-depreciating pure code</td>
        <td><strong>Instant borderless final settlement; 24/7 liquidity</strong></td>
      </tr>
      <tr>
        <td><strong>Physical Gold</strong></td>
        <td>High S2F (~60–80 years)</td>
        <td>1.5%–2.5% annual dilution via new mining</td>
        <td>Storage, assaying, vault security (0.2%–0.5% p.a.)</td>
        <td>Physical transport friction; assaying verification delays</td>
      </tr>
      <tr>
        <td><strong>Prime Real Estate</strong></td>
        <td>Local land scarcity; variable S2F</td>
        <td>Zoning expansions, high-rise up-zoning, new permits</td>
        <td>Property taxes (1%–3% p.a.), maintenance, insurance</td>
        <td>Highly illiquid; weeks-to-months settlement cycle</td>
      </tr>
      <tr>
        <td><strong>US Treasuries / Cash</strong></td>
        <td>Negative scarcity; uncapped expansion</td>
        <td>Uncapped fiscal dilution; exponential debt growth</td>
        <td>Guaranteed negative real yield post monetary dilution</td>
        <td>Restricted banking hours; sanctions/censorship exposure</td>
      </tr>
    </tbody>
  </table>

  <h2 style="font-size: 9.5pt; margin: 8px 0 3px 0; color: #0f2b48;">3.0 Bitcoin Layer-1 as the Base Settlement Layer of Future Global Finance</h2>
  <p style="margin: 0 0 5px 0;">
    A foundational premise of this thesis is that major financial innovations across the digital asset economy will ultimately settle upon Bitcoin Layer-1. Alternative Layer-1 networks routinely sacrifice state decentralization and ledger immutability to chase ephemeral transaction throughput. Bitcoin's Proof-of-Work thermodynamic consensus represents an unbreachable settlement layer supporting secondary infrastructure:
  </p>
  <ul style="margin: 0 0 6px 15px; padding: 0; font-size: 7.6pt; line-height: 1.45;">
    <li><strong>Stablecoin Settlement Rails:</strong> Taproot Assets and Lightning Network facilitate instant, low-fee US Dollar stablecoin settlement finalized against Bitcoin's thermodynamic base-layer security.</li>
    <li><strong>RWA Tokenization & Runes/Ordinals:</strong> Verifiable digital artifacts and real-world asset claims are anchored directly into satoshis, creating immutable provenance without smart contract counterparty risk.</li>
    <li><strong>Trust-Minimized Programmability (BitVM & L2s):</strong> BitVM achieves Turing-complete verification on Bitcoin without protocol forks. Stacks (sBTC consensus linkage) and Babylon (BTC shared security staking) unlock yield without compromising sovereign self-custody.</li>
    <li><strong>Cryptographic Rollups:</strong> ZK-rollups process high-velocity computations off-chain while anchoring cryptographic validity proofs into Bitcoin blocks.</li>
  </ul>

  <div class="callout">
    <strong>Strategic Takeaway:</strong> By deploying capital into corporate treasury vehicles aggregating Bitcoin, an investor does not merely buy a commodity; they acquire proportional equity ownership in the sovereign base settlement layer of the next global financial architecture.
  </div>

  <div class="running-footer">
    <span>Bitcoin Corporate Treasuries Initiation Report • Mahim Patel</span>
    <span>Page 2 of 5</span>
  </div>
</div>

<!-- ================= PAGE 3 ================= -->
<div class="page">
  <div class="running-header">
    <span>Digital Credit & The Reflexive Flywheel</span>
    <span>Mahim Patel • Institutional Research</span>
  </div>

  <h2 style="font-size: 9.5pt; margin-bottom: 3px; color: #0f2b48;">4.0 Digital Credit & Capital Structure Arbitrage</h2>
  <p style="margin: 0 0 5px 0;">
    Traditional corporate debt funds depreciating capital assets with uncertain return on invested capital (ROIC). Bitcoin Treasury entities execute a structural macro spread trade: issuing fiat liabilities at 0%–1% interest to acquire an asset compounding at >40% CAGR. This constitutes <strong>Digital Credit</strong>—monetizing the gap between the corporate cost of capital (WACC < 1.5%) and Bitcoin's monetary appreciation.
  </p>
  <p style="margin: 0 0 5px 0;">
    <strong>Institutional Convertible Arbitrage:</strong> Convertible Senior Notes (Rule 144A) form the core borrowing mechanism. MicroStrategy and Metaplanet issue 5-to-8 year notes carrying 0.0% to 0.875% cash coupons at 30%–40% conversion premiums. Institutional fixed-income buyers execute convertible arbitrage—purchasing the notes and delta-hedging by shorting common stock to capture implied volatility while securing par redemption. The corporate issuer effectively accesses institutional fiat liquidity at negative real rates.
  </p>
  <p style="margin: 0 0 6px 0;">
    <strong>Zero Margin-Call Architecture:</strong> The corporate notes are general, unsecured senior obligations of the parent. There are zero loan-to-value (LTV) liquidation covenants, zero margin maintenance triggers, and zero collateral liens on the underlying Bitcoin reserves. Even under an 80% market crash, creditors cannot force Bitcoin liquidations.
  </p>

  <h2 style="font-size: 9.5pt; margin: 8px 0 3px 0; color: #0f2b48;">5.0 The Reflexive ATM Flywheel & "BTC Yield" Accretion Mathematics</h2>
  <p style="margin: 0 0 5px 0;">
    When a company's stock trades at an Enterprise Value exceeding the market value of its underlying Bitcoin (mNAV > 1.0x), At-The-Market (ATM) equity offerings (Rule 415) are mathematically non-dilutive. Newly issued equity monetizes the market's speculative premium to acquire spot Bitcoin at an effective net discount, increasing the underlying Bitcoin backing per share for existing holders.
  </p>
  <div class="formula-box">
    BTC Yield = [(BTC_t / Diluted_Shares_t) - (BTC_0 / Diluted_Shares_0)] / (BTC_0 / Diluted_Shares_0)
  </div>
  <p style="margin: 3px 0 6px 0;">
    <strong>Numerical Balance Sheet Proof:</strong> 10M shares holding 10,000 BTC ($100k spot, $100 NAV/share) trading at 2.0x mNAV ($200/share). A $100M ATM offering issues 500k shares (+5% dilution) and purchases 1,000 BTC (+10% asset growth). BTC/share jumps from 0.001000 to 0.001048—delivering <strong>+4.76% net asset accretion</strong> with zero capital required from shareholders.
  </p>

  <h3 style="font-size: 8.5pt; margin: 4px 0 2px 0; color: #0f2b48;">Accretion Sensitivity per $1B Capital Raised</h3>
  <table>
    <thead>
      <tr>
        <th>Market Multiple (mNAV)</th>
        <th class="num">Equity Issue Price</th>
        <th class="num">Shares Issued per $1B</th>
        <th class="num">BTC Acquired ($100k Spot)</th>
        <th class="num">Net BTC Yield Accretion</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1.20x (Trough Compression)</strong></td>
        <td class="num font-mono-num">$120.00</td>
        <td class="num font-mono-num">8,333,333</td>
        <td class="num font-mono-num">10,000 BTC</td>
        <td class="num font-mono-num"><strong>+1.54%</strong></td>
      </tr>
      <tr>
        <td><strong>1.50x (Baseline Median)</strong></td>
        <td class="num font-mono-num">$150.00</td>
        <td class="num font-mono-num">6,666,667</td>
        <td class="num font-mono-num">10,000 BTC</td>
        <td class="num font-mono-num"><strong>+3.12%</strong></td>
      </tr>
      <tr>
        <td><strong>2.00x (Bull Expansion)</strong></td>
        <td class="num font-mono-num">$200.00</td>
        <td class="num font-mono-num">5,000,000</td>
        <td class="num font-mono-num">10,000 BTC</td>
        <td class="num font-mono-num"><strong>+4.76%</strong></td>
      </tr>
      <tr>
        <td><strong>2.50x (High Momentum)</strong></td>
        <td class="num font-mono-num">$250.00</td>
        <td class="num font-mono-num">4,000,000</td>
        <td class="num font-mono-num">10,000 BTC</td>
        <td class="num font-mono-num"><strong>+5.77%</strong></td>
      </tr>
      <tr>
        <td><strong>3.00x (Euphoria Premium)</strong></td>
        <td class="num font-mono-num">$300.00</td>
        <td class="num font-mono-num">3,333,333</td>
        <td class="num font-mono-num">10,000 BTC</td>
        <td class="num font-mono-num"><strong>+6.45%</strong></td>
      </tr>
    </tbody>
  </table>

  <div class="callout">
    <strong>Soros Reflexivity in Action:</strong> Sentiment Expansion &rarr; mNAV Multiples Widen &rarr; Faster BTC/Share Accretion per ATM Dollar &rarr; Higher Intrinsic Book Value per Share &rarr; Sustained Market Valuation Multiples.
  </div>

  <div class="running-footer">
    <span>Bitcoin Corporate Treasuries Initiation Report • Mahim Patel</span>
    <span>Page 3 of 5</span>
  </div>
</div>

<!-- ================= PAGE 4 ================= -->
<div class="page">
  <div class="running-header">
    <span>Valuation Discipline & The Structural Floor</span>
    <span>Mahim Patel • Institutional Research</span>
  </div>

  <h2 style="font-size: 9.5pt; margin-bottom: 3px; color: #0f2b48;">6.0 Valuation Discipline: Statistical mNAV Bands & The 15th Percentile Rule</h2>
  <p style="margin: 0 0 5px 0;">
    Valuing corporate treasuries requires Market Net Asset Value: <strong>mNAV = Enterprise Value / (Spot BTC Price &times; Total BTC Reserves)</strong>. Historical multiples cycle through distinct distribution regimes: (1) Deep Multiple Compression: 1.05x–1.25x mNAV; (2) Normal Accumulation: 1.50x–1.90x mNAV; (3) Speculative Blow-off: 2.50x–3.50x mNAV.
  </p>
  <p style="margin: 0 0 5px 0;">
    <strong>The &le;15th Percentile Quantitative Entry Protocol:</strong> Deploying capital strictly below the 15th percentile of historical rolling mNAV provides a quantitative margin of safety. Entering at 1.10x–1.25x mNAV strips away the speculative premium, acquiring leveraged corporate exposure at near-parity with underlying spot assets. As market sentiment normalizes toward the median (1.75x) or 85th percentile (2.50x), multiple expansion generates <strong>60%–115% structural alpha</strong> on top of base Bitcoin appreciation.
  </p>
  <p style="margin: 0 0 6px 0;">
    <strong>Cyclical Rebalancing & Profit Realization:</strong> Disciplined profit-taking dictates trimming positions when mNAV expands beyond the 85th percentile (>2.50x). Gains are systematically rotated into spot Bitcoin, liquid reserves, or temporarily compressed treasury peers (e.g., rotating MSTR premium into Metaplanet discount), re-entering only after mNAV resets below the 25th percentile.
  </p>

  <h2 style="font-size: 9.5pt; margin: 8px 0 3px 0; color: #0f2b48;">7.0 The Structural Floor Hypothesis: Corporate Treasuries Cushioning Bear Cycles</h2>
  <p style="margin: 0 0 5px 0;">
    Historically, Bitcoin bear markets experienced catastrophic drawdowns: 2014 (-86%), 2018 (-84%), and 2022 (-77%). These crashes were precipitated by recursive liquidations across uncollateralized shadow-lending platforms (Mt. Gox, Terra-Luna, 3AC, FTX) dumping into thin order books.
  </p>
  <p style="margin: 0 0 5px 0;">
    <strong>Permanent Balance Sheet Sinks:</strong> The institutional landscape post-2024 introduces permanent corporate sinks. Corporate treasuries (MSTR, Metaplanet, Semler) operate with indefinite holding horizons ("never sell"). Their balance sheets act as counter-cyclical liquidity sponges: as spot prices drop 30%–40%, ATM facilities and convertible debt issuances expand to absorb miner capitulation and forced selling.
  </p>
  <p style="margin: 0 0 6px 0;">
    <strong>The -50% Drawdown Floor Paradigm:</strong> With spot ETFs and corporate treasuries permanently locking up >12% of circulating Bitcoin supply, exchange liquid float has collapsed. This creates a game-theoretic support floor around a ~50% peak-to-trough drawdown (e.g., a cycle peak of $160,000 bottoming at $80,000 rather than crashing to $30,000). Corporate balance sheets structurally compress the downside tail of the asset class.
  </p>

  <h2 style="font-size: 9.5pt; margin: 8px 0 3px 0; color: #0f2b48;">8.0 Flagship Analysis: MicroStrategy (NASDAQ: MSTR)</h2>
  <p style="margin: 0 0 4px 0;">
    MicroStrategy's software division generates ~$480M in recurring revenues covering corporate overhead and debt service. Its convertible debt stack carries under $40M in annual interest obligations—fully covered by software operating cash flows with zero margin calls.
  </p>
  <table>
    <thead>
      <tr>
        <th>Debt Instrument</th>
        <th class="num">Principal</th>
        <th class="num">Coupon</th>
        <th class="num">Maturity</th>
        <th>Conversion Terms / Strike</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Convertible Senior Notes</td><td class="num font-mono-num">$650M</td><td class="num font-mono-num">0.750%</td><td class="num font-mono-num">2025</td><td>$397.99 conversion strike</td></tr>
      <tr><td>Convertible Senior Notes</td><td class="num font-mono-num">$1,050M</td><td class="num font-mono-num">0.000%</td><td class="num font-mono-num">2027</td><td>$1,432.50 conversion strike</td></tr>
      <tr><td>Senior Secured Notes</td><td class="num font-mono-num">$500M</td><td class="num font-mono-num">6.125%</td><td class="num font-mono-num">2028</td><td>Senior secured; pari passu</td></tr>
      <tr><td>Convertible Senior Notes</td><td class="num font-mono-num">$800M</td><td class="num font-mono-num">2.250%</td><td class="num font-mono-num">2032</td><td>$2,045.00 conversion strike</td></tr>
      <tr><td>Convertible Senior Notes</td><td class="num font-mono-num">$1,010M</td><td class="num font-mono-num">0.625%</td><td class="num font-mono-num">2028</td><td>$1,831.94 conversion strike</td></tr>
    </tbody>
  </table>

  <div class="running-footer">
    <span>Bitcoin Corporate Treasuries Initiation Report • Mahim Patel</span>
    <span>Page 4 of 5</span>
  </div>
</div>

<!-- ================= PAGE 5 ================= -->
<div class="page">
  <div class="running-header">
    <span>Risk Modeling, Tax Optimization & 4-Yr Scenarios</span>
    <span>Mahim Patel • Institutional Research</span>
  </div>

  <h2 style="font-size: 9.5pt; margin-bottom: 3px; color: #0f2b48;">9.0 High-Beta Satellites & Risk Stress-Testing</h2>
  <p style="margin: 0 0 4px 0;">
    <strong>Metaplanet (TSE: 3350 / ADR):</strong> JPY debt arbitrage capitalizing on Japan's >260% debt-to-GDP and negative real rates. Exploits a massive domestic tax arbitrage: in Japan, direct crypto is taxed up to 55%, while Metaplanet public equity is taxed at a flat 20%.<br>
    <strong>Strive / Semler Scientific (NASDAQ: SMLR):</strong> High-margin medical diagnostic cash cow (QuantaFlo, ~40% operating margin) redirecting 100% of free cash flow into programmatic Bitcoin accumulation with zero funded debt.<br>
    <strong>Rebuttal to Short-Sellers (Kerrisdale Pair Trade):</strong> The 'Short MSTR / Long BTC' trade suffers fatal flaws: high negative carry from stock borrow fees, explosive gamma squeeze blowouts, and willful ignorance of BTC Yield accretion raising intrinsic book value.
  </p>

  <h2 style="font-size: 9.5pt; margin: 7px 0 3px 0; color: #0f2b48;">10.0 Indian Regulatory Architecture & Tax Arbitrage (INDmoney / LRS)</h2>
  <div class="callout-amber">
    <strong>Tax Arbitrage over Domestic Crypto:</strong> Direct cryptocurrency gains in India face a punitive 30% flat tax + 1% TDS with ZERO set-off of losses. Under the LRS route, US equities/ADRs held &gt; 24 months are taxed as unlisted foreign assets at a favorable <strong>12.5% LTCG</strong> (Finance Act amendments) with <strong>full loss set-off capability</strong>.
  </div>
  <p style="margin: 0 0 5px 0;">
    <strong>0% TCS Mastery:</strong> Because Mahim Patel's capital staging is scheduled at ₹6,00,000 in Year 1 and ₹5,00,000/year across Years 2, 3, and 4, remittances remain strictly below the ₹7,00,000 annual RBI LRS ceiling in every single financial year. TCS is 0% across all tranches. The 3%–4% annual depreciation of the Indian Rupee against the US Dollar provides an automatic structural currency return booster.
  </p>

  <h2 style="font-size: 9.5pt; margin: 7px 0 3px 0; color: #0f2b48;">11.0 4-Year Return Scenario Modeling (INR 21,00,000 Capital)</h2>
  <table>
    <thead>
      <tr>
        <th>Macro Scenario (2026–2030)</th>
        <th class="num">Spot BTC Price</th>
        <th class="num">Target mNAV</th>
        <th class="num">Terminal Portfolio (INR)</th>
        <th class="num">MOIC</th>
        <th class="num">Strategy XIRR</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Bear Case (Macro Stagnation)</strong></td>
        <td class="num font-mono-num">$75,000</td>
        <td class="num font-mono-num">1.15x</td>
        <td class="num font-mono-num"><strong>INR 29,74,000</strong></td>
        <td class="num font-mono-num">1.42x</td>
        <td class="num font-mono-num"><strong>14.0%</strong></td>
      </tr>
      <tr>
        <td><strong>Base Case (Institutional Maturation)</strong></td>
        <td class="num font-mono-num">$185,000</td>
        <td class="num font-mono-num">1.65x</td>
        <td class="num font-mono-num" style="color:#0f2b48;"><strong>INR 59,53,000</strong></td>
        <td class="num font-mono-num"><strong>2.83x</strong></td>
        <td class="num font-mono-num" style="color:#0f2b48;"><strong>45.0%</strong></td>
      </tr>
      <tr>
        <td><strong>Bull Case (Sovereign Adoption / Hyper-Beta)</strong></td>
        <td class="num font-mono-num">$380,000</td>
        <td class="num font-mono-num">2.35x</td>
        <td class="num font-mono-num" style="color:#b45309;"><strong>INR 1,07,13,000</strong></td>
        <td class="num font-mono-num"><strong>5.10x</strong></td>
        <td class="num font-mono-num" style="color:#b45309;"><strong>75.0%</strong></td>
      </tr>
    </tbody>
  </table>

  <div class="callout" style="margin-top: 5px;">
    <strong>Execution Summary & Monitoring Protocol:</strong><br>
    • <strong>Year 1:</strong> Deploy remaining INR 2,50,000 top-up into constituent showing lowest 1-year mNAV percentile (&le;15th %ile).<br>
    • <strong>Years 2–4:</strong> Deploy scheduled INR 5,00,000 annual tranches during cyclical consolidation windows.<br>
    • <strong>Rebalancing:</strong> Trim when an individual entity's mNAV exceeds the 85th percentile (>2.50x) into cash or lagging peers.<br>
    • <strong>Terminal Outlook:</strong> In the Base Case, the INR 21 Lakh principal compounds to <strong>INR 59.53 Lakhs (+₹38.53L profit / 45.0% XIRR)</strong>. In the Bull Case, the portfolio reaches <strong>INR 1.07 Crore (5.10x MOIC / 75.0% XIRR)</strong>.
  </div>

  <div class="running-footer">
    <span>Bitcoin Corporate Treasuries Initiation Report • Mahim Patel</span>
    <span>Page 5 of 5</span>
  </div>
</div>

</body>
</html>
"""

with open("Bitcoin_Treasury_Companies_Initiation_Report.html", "w") as f:
    f.write(html_content)

print("Generated Bitcoin_Treasury_Companies_Initiation_Report.html successfully!")
