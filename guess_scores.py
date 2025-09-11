import random
from pathlib import Path
SCORES = Path("guess_scores.txt")
RANGES = {"1" : 20, "2" :50, "3" : 100}
LABELS = {20: "Easy", 50: "Medium", 100: "Hard"}
def load_scores():
    best = {20: None, 50: None, 100: None}
    if SCORES.exists():
        for line in SCORES.read_text().splitlines():
            try:
                level, tries = line.split(",")
                best[int(level)] = int(tries)
            except ValueError:
                continue
    return best
def save_scores(best):
    text = "\n".join(f"{level},{tries}" for level, tries in best.items() if tries is not None)
    SCORES.write_text(text, encoding="utf-8")
def pick_range():
    print("choose Difficulty: [1] Easy (1-20), [2] Medium (1-50), [3] Hard (1-100)")
    choice =input(">").strip()
    return choice if choice in RANGES else "3" # default hard if unknown
def play():
    best = load_scores()
    choice = pick_range()
    max_n = RANGES[choice]
    secret = random.randint(1, max_n)
    tries = 0
    print(f"Welcome to the Guess the Number Game! (1-{max_n}).")
    if best[max_n] is not None:
        print(f"Best score for {LABELS[max_n]} is {best[max_n]} tries.")
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
            if best[max_n] is None or tries < best[max_n]:
                best[max_n] = tries
                print("New Best Score!")
                save_scores(best)
            break
if __name__ == "__main__":
    play()