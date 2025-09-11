import random
def play():
    secret = random.randint(1, 100)
    tries = 0
    print("Welcome to the Guess the Number Game!")
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            tries += 1
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret} in {tries} tries.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
if __name__ == "__main__":
    play()            
        