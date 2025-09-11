import random
RANGES = {"1" : 20, "2" :50, "3" : 100}
def pick_range():
    print("choose Difficulty: [1] Easy (1-20), [2] Medium (1-50), [3] Hard (1-100)")
    choice =input(">").strip()
    return RANGES.get(choice, 100) # default hard if unknown
def play():
    max_n = pick_range()
    secret = random.randint(1, max_n)
    tries = 0
    print(f"Welcome to the Guess the Number Game! (1-{max_n}).")
    while True:
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Enter A Whole Number!!!")
            continue
        tries += 1
        if guess < secret:
            print("You guessed too low! Try Again.")
        elif guess > secret:
            print("You guessed too high! Try Again.")
        else:
            print(f"Congratulations!🎉🎊 You've guessed the number {secret} in {tries} tries.")
            break
if __name__ == "__main__":
    play()