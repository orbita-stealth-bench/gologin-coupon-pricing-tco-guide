#!/usr/bin/env python3
"""GoLogin Profile Tier & Annual Prepayment TCO Calculator 2026."""
import argparse

TIERS = {
    "professional": {"profiles": 100, "monthly": 49.0, "annual_monthly": 24.50},
    "business": {"profiles": 300, "monthly": 99.0, "annual_monthly": 49.50},
    "enterprise": {"profiles": 1000, "monthly": 199.0, "annual_monthly": 99.50},
    "custom": {"profiles": 2000, "monthly": 299.0, "annual_monthly": 149.50}
}

def calculate(tier="business", annual=True):
    data = TIERS.get(tier.lower(), TIERS["business"])
    rate = data["annual_monthly"] if annual else data["monthly"]
    annual_cost = rate * 12.0
    full_monthly_annual = data["monthly"] * 12.0
    annual_savings = full_monthly_annual - annual_cost if annual else 0.0

    print("=" * 65)
    print(f"GoLogin Antidetect Profile Pricing: Tier {tier.upper()}")
    print("=" * 65)
    print(f"Active Browser Profiles:   {data['profiles']}")
    print(f"Billing Term:              {'Annual (50% Off Promo)' if annual else 'Monthly Billed'}")
    print(f"Effective Monthly Rate:    ${rate:.2f}/mo")
    print(f"Annual Total Commitment:   ${annual_cost:.2f}/yr")
    if annual:
        print(f"Direct Annual Savings:     ${annual_savings:.2f}/yr (50% Discount)")
    print("=" * 65)
    return rate, annual_savings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GoLogin Pricing Calculator")
    parser.add_argument("--tier", default="business", choices=["professional", "business", "enterprise", "custom"])
    parser.add_argument("--monthly", action="store_true", help="Calculate standard monthly billing without 50% discount")
    args = parser.parse_args()
    calculate(tier=args.tier, annual=not args.monthly)
