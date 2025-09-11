def calc_total(bill, tip_percent=15, people=1):
    tip_amount = bill * (tip_percent / 100)
    total = bill * (tip_percent / 100) + bill
    per_person =total / people
    return tip_amount, total, per_person
if __name__ == "__main__":
    try:
        bill = float(input("Enter bill amount: "))
        tip_percent = float(input("Enter tip percentage (default 15%): ") or "15")
        people = int(input("How many people? (default 1): ") or "1")
        tip, total, per_person = calc_total(bill, tip_percent, people)  
        print(f"\nTip amount: ${tip:.2f}")
        print(f"Total amount: ${total:.2f}")
        print(f"Amount per person: ${per_person:.2f}")
    except ValueError:
        print("❌ Please enter valid numbers.")