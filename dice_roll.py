import random
def roll_dice(count=1, sides=6):
    rolls = [random.randint(1, sides) for _ in range(count)]
    return rolls, sum(rolls)
if __name__ == "__main__":
    try:
        how_many = int(input("How many dice? (default 1): ") or "1")
        sides = int(input("how many sides? (default 6): ") or "6")
        rolls, total = roll_dice(how_many, sides)
        print(f"Rolls: {rolls}")
        print(f"total: {total}")
    except ValueError:
        print("please enter whole numbers only.")        
