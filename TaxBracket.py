# Exercise 4: Tax Bracket Determiner
# Uses functions to return tax bracket and estimate tax owed

def get_tax_bracket(income: float) -> str:
    """
    Returns tax bracket as a string.
    Uses a ternary expression to mark deduction eligibility.
    """
    if income < 0:
        return "Invalid income."

    if income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)"
        rate = 0.30

    eligible = " (Deduction Eligible)" if income % 2 == 0 else ""
    return bracket + eligible, rate


# ---- Main Program ----
try:
    income = float(input("What's your annual income? ").strip())
except ValueError:
    print("Invalid input.")
    exit()

result = get_tax_bracket(income)

if isinstance(result, str):
    print(result)
else:
    bracket, rate = result
    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax:.2f}")
