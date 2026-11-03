import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
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

doc = docx.Document()

# Page setup: 0.7 in margins (Institutional density)
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.7)
    s.bottom_margin = Inches(0.7)
    s.left_margin = Inches(0.7)
    s.right_margin = Inches(0.7)

# Color Palette
COLOR_NAVY = RGBColor(15, 23, 42)      # #0F172A
COLOR_GOLD = RGBColor(180, 83, 9)       # #B45309
COLOR_MUTED = RGBColor(100, 116, 139)   # #64748B
COLOR_TEXT = RGBColor(30, 41, 59)       # #1E293B

# Header Metadata Block
header_table = doc.add_table(rows=1, cols=2)
header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
header_table.autofit = False

left_cell = header_table.cell(0, 0)
left_cell.width = Inches(5.0)
p_hdr = left_cell.paragraphs[0]
p_hdr.paragraph_format.space_before = Pt(0)
p_hdr.paragraph_format.space_after = Pt(2)
run_tag = p_hdr.add_run("INSTITUTIONAL EQUITY RESEARCH | DIGITAL ASSETS & CORPORATE TREASURIES\n")
run_tag.font.name = "Calibri"
run_tag.font.size = Pt(8.5)
run_tag.font.bold = True
run_tag.font.color.rgb = COLOR_GOLD

run_title = p_hdr.add_run("Bitcoin Corporate Treasuries Initiation Report\n")
run_title.font.name = "Arial"
run_title.font.size = Pt(17)
run_title.font.bold = True
run_title.font.color.rgb = COLOR_NAVY

run_sub = p_hdr.add_run("Capturing Structural Alpha via Digital Credit, Volatility Monetization & mNAV Discipline")
run_sub.font.name = "Calibri"
run_sub.font.size = Pt(10)
run_sub.font.color.rgb = COLOR_MUTED

right_cell = header_table.cell(0, 1)
right_cell.width = Inches(2.1)
set_cell_background(right_cell, "F8FAFC")
set_cell_margins(right_cell, top=100, bottom=100, left=150, right=150)
p_box = right_cell.paragraphs[0]
p_box.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_box.paragraph_format.space_before = Pt(0)
p_box.paragraph_format.space_after = Pt(1)

def add_meta_line(p, label, val, is_bold_val=False, val_color=COLOR_TEXT):
    r1 = p.add_run(label + ": ")
    r1.font.name = "Calibri"
    r1.font.size = Pt(8.5)
    r1.font.color.rgb = COLOR_MUTED
    r2 = p.add_run(val + "\n")
    r2.font.name = "Calibri"
    r2.font.size = Pt(8.5)
    r2.font.bold = is_bold_val
    r2.font.color.rgb = val_color

add_meta_line(p_box, "Analyst", "Mahim Patel", True, COLOR_NAVY)
add_meta_line(p_box, "Coverage Rating", "HIGH-CONVICTION OVERWEIGHT", True, COLOR_GOLD)
add_meta_line(p_box, "Capital Deployed", "INR 3,50,000 (~$4.2K USD)", True, COLOR_NAVY)
add_meta_line(p_box, "Execution Route", "INDmoney (RBI LRS)", False, COLOR_TEXT)
add_meta_line(p_box, "Target Horizon", "4 Years (2026 – 2030)", True, COLOR_TEXT)
add_meta_line(p_box, "Primary Benchmark", "Spot BTC (BTC/USD)", False, COLOR_MUTED)

# Remove borders for header
set_table_borders(header_table, color="FFFFFF", sz="0", val="none")

# Horizontal Divider Line
p_div = doc.add_paragraph()
p_div.paragraph_format.space_before = Pt(4)
p_div.paragraph_format.space_after = Pt(8)
p_div_run = p_div.add_run("━" * 68)
p_div_run.font.size = Pt(9)
p_div_run.font.color.rgb = COLOR_GOLD

# Section Heading Helper
def add_section_heading(doc, title, number=""):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    if number:
        r_num = h.add_run(number + " ")
        r_num.font.name = "Arial"
        r_num.font.size = Pt(12)
        r_num.font.bold = True
        r_num.font.color.rgb = COLOR_GOLD
    r_txt = h.add_run(title)
    r_txt.font.name = "Arial"
    r_txt.font.size = Pt(12)
    r_txt.font.bold = True
    r_txt.font.color.rgb = COLOR_NAVY

def add_body_p(doc, text, bold_prefix="", italic_prefix="", space_after=4):
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
    if italic_prefix:
        ri = p.add_run(italic_prefix)
        ri.font.name = "Calibri"
        ri.font.size = Pt(9.5)
        ri.font.italic = True
        ri.font.color.rgb = COLOR_TEXT
    rt = p.add_run(text)
    rt.font.name = "Calibri"
    rt.font.size = Pt(9.5)
    rt.font.color.rgb = COLOR_TEXT
    return p

# SECTION 1: EXECUTIVE INITIATION
add_section_heading(doc, "Executive Initiation & Portfolio Allocation Architecture", "1.0")

add_body_p(doc, 
    "This research report initiates coverage on a targeted basket of Bitcoin Corporate Treasury companies (MicroStrategy, Strive/Semler Scientific, and Metaplanet ADR) representing an aggregate capital deployment of INR 3,50,000 via the INDmoney app (RBI Liberalised Remittance Scheme). The strategic objective is not merely beta exposure to Bitcoin price appreciation, but the systematic capture of structural alpha over spot Bitcoin. Over a multi-year horizon (2026–2030), these corporate balance sheets exploit structural market inefficiencies—monetizing equity volatility, issuing ultra-low-cost digital credit, and compounding Bitcoin per share through reflexive At-The-Market (ATM) equity offerings.",
    bold_prefix="Core Proposition: ")

# Portfolio Allocation Table
t_alloc = doc.add_table(rows=4, cols=5)
t_alloc.alignment = WD_TABLE_ALIGNMENT.CENTER
t_alloc.autofit = False
set_table_borders(t_alloc, color="CBD5E1", sz="4", val="single")

headers = ["Holding / Entity", "Ticker / Custody", "Capital (INR)", "Weight (%)", "Strategic Role in Thesis"]
col_widths = [Inches(1.8), Inches(1.3), Inches(1.0), Inches(0.8), Inches(2.2)]

for col_idx, (h_text, w) in enumerate(zip(headers, col_widths)):
    cell = t_alloc.cell(0, col_idx)
    cell.width = w
    set_cell_background(cell, "0F172A")
    set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(h_text)
    r.font.name = "Calibri"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

data = [
    ["MicroStrategy Inc.", "NASDAQ: MSTR (INDmoney)", "INR 1,50,000", "42.9%", "Flagship anchor; S&P 500 inclusion flows; massive ATM liquidity; institutional credit access."],
    ["Strive / Semler Scientific", "NASDAQ: SMLR / Strive", "INR 1,10,000", "31.4%", "Mid/small-cap high beta; operational cash flow redirect into BTC; fast BTC/share growth."],
    ["Metaplanet Inc.", "TSE: 3350 / ADR (INDmoney)", "INR 80,000", "22.8%", "Asian MicroStrategy; JPY debt/yield arbitrage; 20% equity tax vs 55% Japanese crypto tax."]
]

for row_idx, row_data in enumerate(data, start=1):
    bg_color = "FFFFFF" if row_idx % 2 == 1 else "F8FAFC"
    for col_idx, (val, w) in enumerate(zip(row_data, col_widths)):
        cell = t_alloc.cell(row_idx, col_idx)
        cell.width = w
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        if col_idx in [0, 2, 3]:
            r.font.bold = True
            r.font.color.rgb = COLOR_NAVY
        else:
            r.font.color.rgb = COLOR_TEXT

# Three Pillars Callout
p_pill = doc.add_paragraph()
p_pill.paragraph_format.space_before = Pt(6)
p_pill.paragraph_format.space_after = Pt(6)
p_pill.paragraph_format.line_spacing = 1.15
r_p1 = p_pill.add_run("The Investment Thesis is Built on Three Interconnected Quantitative Pillars:\n")
r_p1.font.name = "Calibri"
r_p1.font.size = Pt(9.5)
r_p1.font.bold = True
r_p1.font.color.rgb = COLOR_NAVY

p_p1_text = (
    "1. Monetary Hardness & Fiat Debasement: Accelerating global fiscal deficits force monetary dilution; Bitcoin acts as the apex monetary energy sink.\n"
    "2. Corporate Financial Engineering Alpha (BTC Yield): Issuing zero/low-coupon convertible credit and accretive equity at mNAV > 1.0x permanently increases BTC backing per share.\n"
    "3. Quantitative Entry Discipline (<15th Percentile mNAV): Deploying capital strictly when market net asset value multiples are compressed eliminates premium destruction risk and maximizes cyclical mean-reversion."
)
r_p2 = p_pill.add_run(p_p1_text)
r_p2.font.name = "Calibri"
r_p2.font.size = Pt(9)
r_p2.font.color.rgb = COLOR_TEXT

# SECTION 2: MACRO ARCHITECTURE & MONETARY CAPITAL
add_section_heading(doc, "Macroeconomic Paradigm: Sovereign Debt Spiral & Monetary Debasement", "2.0")

add_body_p(doc,
    "The global macroeconomic backdrop is defined by structural Fiscal Dominance—a regime where sovereign debt levels exceed sustainable thresholds, forcing central banks to prioritize government solvency over currency stability. With US national debt surpassing $35 Trillion (>120% Debt-to-GDP) and annual net interest expense exceeding $1 Trillion (surpassing the entire annual US National Defense authorization), traditional monetary tightening is mathematically self-defeating. Higher interest rates mechanically expand sovereign interest deficits, expanding the money supply through fiscal channels.",
    bold_prefix="The Fiscal Dominance Trap: ")

add_body_p(doc,
    "In this environment, fiat purchasing power decays exponentially. The true inflation rate experienced by capital is not the politically hedged Consumer Price Index (CPI), but the rate of global fiat monetary expansion (M2 CAGR). Mathematically, real purchasing power loss is expressed as: Pt = P0 * (1 - pi_real)^t, where pi_real = (Delta M2 / M2) - Delta Y_real. With global M2 historically expanding at 7%–10% annually, capital held in conventional sovereign debt or cash instruments suffers guaranteed structural debasement.",
    bold_prefix="Mathematical Mechanics of Debasement: ")

# Asset Class Comparison Table
t_asset = doc.add_table(rows=5, cols=5)
t_asset.alignment = WD_TABLE_ALIGNMENT.CENTER
t_asset.autofit = False
set_table_borders(t_asset, color="CBD5E1", sz="4", val="single")

asset_headers = ["Asset Class", "Supply Scarcity / S2F", "Dilution Risk / Elasticity", "Holding / Carry Cost", "Settlement Velocity & Portability"]
asset_widths = [Inches(1.4), Inches(1.4), Inches(1.5), Inches(1.2), Inches(1.6)]

for col_idx, (h_text, w) in enumerate(zip(asset_headers, asset_widths)):
    cell = t_asset.cell(0, col_idx)
    cell.width = w
    set_cell_background(cell, "0F172A")
    set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(h_text)
    r.font.name = "Calibri"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

asset_data = [
    ["Bitcoin (BTC)", "Absolute Scarcity: 21M hard cap; S2F -> Infinity", "Zero supply response to price; strictly inelastic", "Zero storage cost; non-depreciating pure code", "Instant borderless final settlement; 24/7 global liquidity"],
    ["Physical Gold", "High Stock-to-Flow (~60-80 years)", "1.5%–2.5% annual supply dilution via new mining", "Storage, assaying, physical security, insurance costs", "Physical transport friction; assaying verification delays"],
    ["Prime Real Estate", "Local land scarcity; variable S2F", "Permit expansions, up-zoning, localized supply surges", "High maintenance, property taxes (1-3% p.a.), insurance", "Highly illiquid; weeks to months transaction settlement"],
    ["US Treasuries / Fiat", "Negative scarcity; infinite printing capacity", "Uncapped fiscal dilution; sovereign debt compounding", "Guaranteed negative real yield after true monetary dilution", "Restricted banking hours; sanctions/censorship exposure"]
]

for row_idx, row_data in enumerate(asset_data, start=1):
    bg_color = "FFFFFF" if row_idx % 2 == 1 else "F8FAFC"
    for col_idx, (val, w) in enumerate(zip(row_data, asset_widths)):
        cell = t_asset.cell(row_idx, col_idx)
        cell.width = w
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=50, bottom=50, left=90, right=90)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(8)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = COLOR_NAVY
        else:
            r.font.color.rgb = COLOR_TEXT

# SECTION 3: BASE LAYER SETTLEMENT
add_section_heading(doc, "Bitcoin Layer-1 as the Base Settlement Layer of Future Finance", "3.0")

add_body_p(doc,
    "A fundamental premise of this investment thesis is that all major technological expansions across the digital asset ecosystem—stablecoins, tokenization of real-world assets (RWAs), and decentralized finance—will ultimately converge and settle upon Bitcoin Layer-1. Alternative Layer-1 blockchains compromise on decentralization, ledger immutability, and state security to achieve temporary throughput. Bitcoin’s Proof-of-Work thermodynamic consensus represents an impenetrable monetary bedrock upon which secondary execution layers are rapidly maturing:",
    bold_prefix="The Settlement Convergence Thesis: ")

tech_points = [
    ("Stablecoin Rails & Liquidity: ", "Implementation of Taproot Assets and Lightning Network rails enables instant, friction-free US Dollar stablecoin settlement directly collateralized and finalized against Bitcoin’s base-layer thermodynamic security."),
    ("RWA Tokenization & Runes/Ordinals: ", "Verifiable, immutable digital artifacts and real-world asset titles are anchoring ownership records directly into satoshis, creating immutable provenance without smart contract exploit vectors."),
    ("Trust-Minimized Programmability (BitVM & L2s): ", "Architectures like BitVM permit Turing-complete verification on Bitcoin without requiring hard forks. Combined with Stacks (sBTC consensus anchoring) and Babylon (BTC shared security staking), Bitcoin is actively transforming from passive gold into productive, yield-bearing monetary infrastructure."),
    ("Zero-Knowledge & Privacy Rollups: ", "Advanced ZK-rollup frameworks allow complex state transitions and cryptographic privacy to execute off-chain while anchoring final mathematical proof-of-state verification into Bitcoin blocks.")
]

for b_prefix, b_text in tech_points:
    add_body_p(doc, b_text, bold_prefix="• " + b_prefix, space_after=2)

add_body_p(doc,
    "By deploying capital into corporate treasury vehicles that are aggressively aggregating and monetizing Bitcoin reserves, an investor does not merely buy a commodity; they acquire proportional ownership in the sovereign monetary base layer of the next global financial architecture.",
    bold_prefix="Strategic Takeaway: ", space_after=8)

doc.save("Bitcoin_Treasury_Companies_Initiation_Report.docx")
print("Report successfully saved to Bitcoin_Treasury_Companies_Initiation_Report.docx")
