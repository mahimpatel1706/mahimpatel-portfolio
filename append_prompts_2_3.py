import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

# Load existing doc
doc = docx.Document("Bitcoin_Treasury_Companies_Initiation_Report.docx")

COLOR_NAVY = RGBColor(15, 23, 42)      # #0F172A
COLOR_GOLD = RGBColor(180, 83, 9)       # #B45309
COLOR_MUTED = RGBColor(100, 116, 139)   # #64748B
COLOR_TEXT = RGBColor(30, 41, 59)       # #1E293B

def add_section_heading(doc, title, number=""):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(9)
    h.paragraph_format.space_after = Pt(3)
    h.paragraph_format.keep_with_next = True
    if number:
        r_num = h.add_run(number + " ")
        r_num.font.name = "Arial"
        r_num.font.size = Pt(11.5)
        r_num.font.bold = True
        r_num.font.color.rgb = COLOR_GOLD
    r_txt = h.add_run(title)
    r_txt.font.name = "Arial"
    r_txt.font.size = Pt(11.5)
    r_txt.font.bold = True
    r_txt.font.color.rgb = COLOR_NAVY

def add_body_p(doc, text, bold_prefix="", space_after=3.5):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.font.name = "Calibri"
        rb.font.size = Pt(9.5)
        rb.font.bold = True
        rb.font.color.rgb = COLOR_NAVY
    rt = p.add_run(text)
    rt.font.name = "Calibri"
    rt.font.size = Pt(9.5)
    rt.font.color.rgb = COLOR_TEXT
    return p

# SECTION 4.0: DIGITAL CREDIT & CAPITAL STRUCTURE ARBITRAGE
add_section_heading(doc, "Digital Credit & Capital Structure Arbitrage", "4.0")

add_body_p(doc,
    "The primary operational distinction between a passive ETF and an active Bitcoin Treasury corporation lies in capital structure engineering. Traditional corporate debt funds depreciating capital expenditures (e.g., factories, inventory) with highly uncertain hurdle rates. Bitcoin Treasury operators execute a distinct macro arbitrage: issuing fiat-denominated liabilities bearing near-zero coupons to purchase an appreciating, liquid reserve asset. This constitutes 'Digital Credit'—exploiting the structural cost-of-capital spread between melting fiat currencies (WACC < 1.5%) and Bitcoin's multi-year compound annual growth rate (CAGR > 40%).",
    bold_prefix="The Fiat-to-Hard-Asset Spread: ")

add_body_p(doc,
    "Institutional convertible debt issuance (Rule 144A offerings) represents the cornerstone of this strategy. MicroStrategy and Metaplanet issue unsecured convertible senior notes carrying 0.0% to 0.875% cash coupons with 30% to 40% conversion premiums. Institutional buyers of these instruments are not speculative retail traders; they are fixed-income hedge funds executing convertible arbitrage. By purchasing the convertible note and dynamically shorting the underlying common stock, these funds lock in an implied volatility harvest while maintaining par downside protection at maturity. The issuing corporation captures pristine fiat liquidity at effectively negative real interest rates.",
    bold_prefix="Convertible Arbitrage Dynamics: ")

add_body_p(doc,
    "Crucially, this debt architecture is completely unencumbered. The notes are general, unsecured senior obligations of the corporate parent. Unlike crypto-native lending desks (e.g., Celsius, Genesis) that collapsed in 2022 due to rehypothecation and margin liquidation thresholds, these corporate debt facilities feature zero margin call clauses, zero loan-to-value (LTV) triggers, and zero collateral pledges on the underlying Bitcoin reserves. Even during an 80% spot drawdown, no creditor can force asset liquidations.",
    bold_prefix="Unencumbered Custody & Zero Margin-Call Structure: ")

# SECTION 5.0: THE REFLEXIVE ATM FLYWHEEL & BTC YIELD
add_section_heading(doc, "The Reflexive ATM Flywheel & 'BTC Yield' Accretion Mechanics", "5.0")

add_body_p(doc,
    "The engine generating direct shareholder alpha over spot Bitcoin is the At-The-Market (ATM) equity issuance facility. When a corporate treasury's common stock trades at an Enterprise Value greater than the market value of its underlying Bitcoin reserves (mNAV > 1.0x), every dollar of newly issued equity is mathematically accretive to existing shareholders on a per-share basis. The management team continuously monetizes the speculative premium assigned by the equity market to buy physical spot Bitcoin at a net discount.",
    bold_prefix="The ATM Flywheel Condition (mNAV > 1.0x): ")

add_body_p(doc,
    "To measure this performance rigorously, management tracks 'BTC Yield'—the period-over-period percentage accretion in the ratio of total Bitcoin holdings to fully diluted shares outstanding:",
    bold_prefix="Mathematical Definition of BTC Yield: ")

# Formula block
p_form = doc.add_paragraph()
p_form.paragraph_format.space_before = Pt(2)
p_form.paragraph_format.space_after = Pt(4)
p_form.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_f = p_form.add_run("BTC Yield = [(BTC_t / Diluted_Shares_t) - (BTC_0 / Diluted_Shares_0)] / (BTC_0 / Diluted_Shares_0)")
r_f.font.name = "Consolas"
r_f.font.size = Pt(9)
r_f.font.bold = True
r_f.font.color.rgb = COLOR_NAVY

add_body_p(doc,
    "Consider an entity with 10,000,000 shares outstanding holding 10,000 BTC. Spot BTC is $100,000 (NAV per share = $100). The equity trades at an mNAV of 2.0x ($200 per share). The company issues $100M of fresh equity via an ATM offering. Result: exactly 500,000 new shares are issued (5.0% dilution), while $100M proceeds purchase 1,000 new spot BTC (10.0% asset expansion). Total holdings expand to 11,000 BTC across 10,500,000 shares. BTC per share rises from 0.001000 to 0.001048—delivering a +4.76% immediate net accretion in Bitcoin backing per share with zero capital required from existing shareholders.",
    bold_prefix="Numerical Balance Sheet Walkthrough: ")

# Table: Reflexive Accretion Matrix
t_fly = doc.add_table(rows=6, cols=5)
t_fly.alignment = WD_TABLE_ALIGNMENT.CENTER
t_fly.autofit = False
set_table_borders(t_fly, color="CBD5E1", sz="4", val="single")

fly_headers = ["Market Multiple (mNAV)", "Equity Issue Price", "Shares Issued per $1B Raise", "BTC Acquired ($100k Spot)", "Net BTC Yield Accretion (%)"]
fly_widths = [Inches(1.5), Inches(1.3), Inches(1.6), Inches(1.4), Inches(1.3)]

for col_idx, (h_text, w) in enumerate(zip(fly_headers, fly_widths)):
    cell = t_fly.cell(0, col_idx)
    cell.width = w
    set_cell_background(cell, "0F172A")
    set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(h_text)
    r.font.name = "Calibri"
    r.font.size = Pt(8)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

fly_data = [
    ["1.20x (Trough / Compression)", "$120.00", "8,333,333 shares", "10,000 BTC", "+1.54% per share"],
    ["1.50x (Baseline Median)", "$150.00", "6,666,667 shares", "10,000 BTC", "+3.12% per share"],
    ["2.00x (Bull Expansion)", "$200.00", "5,000,000 shares", "10,000 BTC", "+4.76% per share"],
    ["2.50x (High Momentum)", "$250.00", "4,000,000 shares", "10,000 BTC", "+5.77% per share"],
    ["3.00x (Euphoria Premium)", "$300.00", "3,333,333 shares", "10,000 BTC", "+6.45% per share"]
]

for row_idx, row_data in enumerate(fly_data, start=1):
    bg_color = "FFFFFF" if row_idx % 2 == 1 else "F8FAFC"
    for col_idx, (val, w) in enumerate(zip(row_data, fly_widths)):
        cell = t_fly.cell(row_idx, col_idx)
        cell.width = w
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=45, bottom=45, left=80, right=80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(8)
        if col_idx in [0, 4]:
            r.font.bold = True
            r.font.color.rgb = COLOR_NAVY
        else:
            r.font.color.rgb = COLOR_TEXT

add_body_p(doc,
    "This creates textbook Soros reflexivity. Rising market sentiment drives mNAV multiple expansion. A higher mNAV accelerates the rate of accretive BTC accumulation per newly issued share. This accelerated BTC Yield lifts the company's fundamental intrinsic net asset value, justifying institutional capital inflows and sustaining the valuation premium. The investor captures the compounding of spot Bitcoin price plus the continuous compounding of Bitcoin backing per share.",
    bold_prefix="Soros Reflexivity in Corporate Balance Sheets: ", space_after=6)

doc.save("Bitcoin_Treasury_Companies_Initiation_Report.docx")
print("Successfully appended Sections 4.0 and 5.0 to Bitcoin_Treasury_Companies_Initiation_Report.docx")
