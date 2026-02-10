# Exercise 2: Credit Score Evaluator
# Uses conditionals to determine loan eligibility based on credit score

while True:
    try:
        credit_score = int(input("What's your credit score? ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    # Validation
    if credit_score < 300 or credit_score > 850:
        print("Invalid score.\n")
        continue

    # Classification
    if credit_score >= 750:
        result = "Excellent - Loan Approved"
        message = "Interest rate: Low"
    elif credit_score >= 700:
        result = "Good - Loan Approved with Review"
        message = "Interest rate: Low"
    elif credit_score >= 600:
        result = "Fair - Loan Conditional"
        message = "Seek credit improvement."
    else:
        result = "Poor - Loan Denied"
        message = "Seek credit improvement."

    print(f"{result}. {message}\n")

    again = input("Evaluate another score? (y/n): ").strip().lower()
    if again != "y":
        break
