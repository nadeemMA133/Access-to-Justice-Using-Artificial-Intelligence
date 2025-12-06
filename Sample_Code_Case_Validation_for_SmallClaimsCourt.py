from datetime import datetime

def get_date_input(prompt):
    """Get a date from the user in YYYY-MM-DD format."""
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    # 1. Get case filing date
    filing_date = get_date_input("Enter case filing date (YYYY-MM-DD): ")
    current_date = datetime.now()
    time_diff_years = (current_date - filing_date).days / 365.25

    # 2. Check if 3 years old for priority
    priority = time_diff_years >= 3

    if priority:
        print("\n⚠️ Case is 3 years or older — marking as PRIORITY.")
    else:
        print("\nCase is not priority.")

    # 3. Get dispute amount
    while True:
        try:
            amount = float(input("\nEnter dispute amount in dollars: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # 4. Decision branch based on dispute amount
    if amount > 35000:
        print("\n💼 Dispute over $35,000 — Routing case to a judge.")
        return  # End process here

    # 5. For amount ≤ $35,000, collect extra info
    print("\n💰 Dispute is $35,000 or less — collecting additional details...")

    nature = input("Enter nature of the dispute: ")
    dispute_area = input("Enter dispute area: ")
    while True:
        try:
            num_parties = int(input("Enter number of parties involved: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # 6. Route to AI engine
    print("\n🤖 Sending case to AI engine for decision...")
    print("----- Case Summary -----")
    print(f"Priority: {'Yes' if priority else 'No'}")
    print(f"Amount: ${amount:,.2f}")
    print(f"Nature: {nature}")
    print(f"Dispute Area: {dispute_area}")
    print(f"Number of Parties: {num_parties}")
    print("------------------------")

if __name__ == "__main__":
    main()