# Exercise 5: Product Category Matcher
# Uses match-case and string comparisons to categorize products

product = input("What's the product name? ").strip().lower()

match product:
    case p if p.startswith("tech") or p in ("electronics", "gadget"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

print(f"Product: {product} | Category: {category}")
