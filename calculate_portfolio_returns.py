import numpy as np
import numpy_financial as npf

# Capital Deployment Schedule (INR Lakhs)
# T0 (Initial): 3.5 L
# T0.5 (Later Year 1): 2.5 L  (Total Year 1 = 6.0 L)
# T1 (Year 2): 5.0 L
# T2 (Year 3): 5.0 L
# T3 (Year 4): 5.0 L
# Total Principal = 21.0 Lakhs

# Let's model annual cash flows over 4-year horizon (Years 0, 1, 2, 3 -> Terminal at Year 4)
# Cash flows from investor perspective (negative = investment):
# Year 0: -6.0 L
# Year 1: -5.0 L
# Year 2: -5.0 L
# Year 3: -5.0 L
# Year 4: Terminal Value

# Scenario Assumptions:
# Annualized Return of the Strategy (combining Spot BTC + BTC Yield Accretion + mNAV multiple expansion + USD/INR ~3.5% tailwind):
# 1. Bear Case (Extended Stagnation / Sluggish Cycle):
#    Spot BTC reaches $75k by 2030 (low CAGR ~8%), mNAV ~1.15x, BTC Yield ~5% p.a.
#    Net Portfolio Annualized Compound Growth Rate (INR) ~ 14.0%
# 2. Base Case (Institutional Supercycle / Adoption):
#    Spot BTC reaches $185k by 2030 (CAGR ~25%), mNAV ~1.65x, BTC Yield ~12% p.a.
#    Net Portfolio Annualized Compound Growth Rate (INR) ~ 45.0%
# 3. Bull Case (Sovereign Adoption / Hyper-Reflexivity):
#    Spot BTC reaches $380k by 2030 (CAGR ~45%), mNAV ~2.35x, BTC Yield ~20% p.a.
#    Net Portfolio Annualized Compound Growth Rate (INR) ~ 75.0%

def calc_terminal_and_xirr(annual_rate):
    # Year 0 (6.0 L deployed, compounds for 4 years)
    # Year 1 (5.0 L deployed, compounds for 3 years)
    # Year 2 (5.0 L deployed, compounds for 2 years)
    # Year 3 (5.0 L deployed, compounds for 1 year)
    v0 = 6.0 * ((1 + annual_rate) ** 4)
    v1 = 5.0 * ((1 + annual_rate) ** 3)
    v2 = 5.0 * ((1 + annual_rate) ** 2)
    v3 = 5.0 * ((1 + annual_rate) ** 1)
    terminal_val = v0 + v1 + v2 + v3
    
    # Cash flows for IRR
    cfs = [-6.0, -5.0, -5.0, -5.0, terminal_val]
    irr = npf.irr(cfs)
    return terminal_val, irr

scenarios = {
    "Bear Case": 0.14,
    "Base Case": 0.45,
    "Bull Case": 0.75
}

print(f"{'Scenario':<12} | {'Annual Strategy Return':<22} | {'Total Invested':<14} | {'Terminal Value (INR)':<22} | {'Portfolio IRR':<14} | {'MOIC (Multiple)':<14}")
print("-" * 105)
for name, rate in scenarios.items():
    term, irr = calc_terminal_and_xirr(rate)
    moic = term / 21.0
    print(f"{name:<12} | {rate*100:>20.1f}% | INR 21.0 Lakhs | INR {term:>18.2f} L | {irr*100:>12.1f}% | {moic:>12.2f}x")
