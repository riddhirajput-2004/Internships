"""
Tax Deduction Calculator
This program calculates tax deductions under both Old and New tax regimes based on user's CTC and bonus.
"""

def calculate_old_regime_tax(taxable_income):
    """
    Calculate tax as per Old Regime with standard deductions
    """
    # Standard deduction for Old Regime
    taxable_income -= 50000
    
    # 80C deduction (maximum of 1,50,000)
    if taxable_income > 150000:
        taxable_income -= 150000
    else:
        taxable_income = 0
    
    # Tax slabs for Old Regime (FY 2024-25)
    if taxable_income <= 250000:
        return 0
    elif taxable_income <= 500000:
        return (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        return 12500 + (taxable_income - 500000) * 0.2
    else:
        return 112500 + (taxable_income - 1000000) * 0.3

def calculate_new_regime_tax(taxable_income):
    """
    Calculate tax as per New Regime (no deductions)
    """
    # Tax slabs for New Regime (FY 2024-25)
    if taxable_income <= 300000:
        return 0
    elif taxable_income <= 600000:
        return (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        return 15000 + (taxable_income - 600000) * 0.1
    elif taxable_income <= 1200000:
        return 45000 + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        return 90000 + (taxable_income - 1200000) * 0.2
    else:
        return 150000 + (taxable_income - 1500000) * 0.3

def format_currency(amount):
    """Format numbers as currency with commas"""
    return "Rs.{:,.2f}".format(amount).replace(".00", "")

def main():
    print("\nTax Deduction Calculator\n" + "=" * 25)
    
    while True:
        try:
            # Get user input
            ctc = float(input("Enter your CTC: "))
            bonus = float(input("Enter your Bonus: "))
            
            # Calculate total income
            total_income = ctc + bonus
            print(f"\nTotal Income: {format_currency(total_income)}")
            
            # Calculate taxes
            old_tax = calculate_old_regime_tax(total_income)
            new_tax = calculate_new_regime_tax(total_income)
            
            # Display results
            print(f"\nOld Regime Tax Deduction: {format_currency(old_tax)}")
            print(f"New Regime Tax Deduction: {format_currency(new_tax)}")
            
            # Compare regimes
            if old_tax < new_tax:
                savings = new_tax - old_tax
                print(f"\nYou Save {format_currency(savings)} more using the Old Regime.")
            elif new_tax < old_tax:
                savings = old_tax - new_tax
                print(f"\nYou Save {format_currency(savings)} more using the New Regime.")
            else:
                print("\nBoth regimes result in the same tax amount.")
            
            # Menu for continuing or exiting
            choice = input("\nWould you like to calculate again? (y/n): ").lower()
            if choice != 'y':
                print("\nThank you for using the Tax Deduction Calculator!")
                break
                
        except ValueError:
            print("Please enter valid numbers only. Try again.\n")

if __name__ == "__main__":
    main()
