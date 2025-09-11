import random
from pathlib import Path

SCORES = Path("guess_scores.txt")
RANGES = {"1": 20, "2": 50, "3": 100}
LABELS = {"1": "Easy", "2": "Medium", "3": "Hard"}

def load_scores():
    best = {}
    if SCORES.exists():
        for line in SCORES.read_text(encoding="utf-8").splitlines():
            if ":" in line:
                key, tries = line.split(":", 1)
                best[key.strip()] = int(tries.strip())
    return best

def save_scores(best):
    text = "\n".join(f"{k}: {v}" for k, v in best.items())
    if text:
        text += "\n"
    SCORES.write_text(text, encoding="utf-8")

def pick_mode():
    print("\nChoose difficulty:")
    print("[1] Easy (1–20)   [2] Medium (1–50)   [3] Hard (1–100)")
    c = input("> ").strip()
    return c if c in RANGES else "3"

def pick_lives():
    """Return number of guesses allowed, or 0 for unlimited."""
    ans = input("Limit guesses? Enter number (or press Enter for unlimited): ").strip()
    if not ans:
        return 0
    try:
        n = int(ans)
        return max(1, n)
    except ValueError:
        print("Using unlimited.")
        return 0

def play_round(mode, lives, best):
    max_n = RANGES[mode]
    label = LABELS[mode]
    secret = random.randint(1, max_n)
    tries = 0

    print(f"\n{label}: Guess the number (1–{max_n}).")
    key = f"best_{mode}"
    if key in best:
        print(f"Current best for {label}: {best[key]} tries. Beat it!")

    while True:
        if lives:
            print(f"(Lives left: {lives})")
        try:
            guess = int(input("Your guess: ").strip())
        except ValueError:
            print("Enter a whole number.")
            continue

        tries += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"🎉 Correct! {tries} tries.")
            if key not in best or tries < best[key]:
                best[key] = tries
                save_scores(best)
                print("🏆 New personal best!")
            return

        if lives:
            lives -= 1
            if lives == 0:
                print(f"💀 Out of lives. The number was {secret}.")
                return

def main_menu():
    best = load_scores()
    while True:
        print("\n=== Number Guessing Game ===")
        print("[1] Play")
        print("[2] Show Best Scores")
        print("[3] Reset Scores")
        print("[4] Quit")
        choice = input("> ").strip()

        if choice == "1":
            mode = pick_mode()
            lives = pick_lives()
            play_round(mode, lives, best)
        elif choice == "2":
            if not best:
                print("No scores yet.")
            else:
                for k, v in best.items():
                    label = LABELS[k[-1]] if k.startswith("best_") and k[-1] in LABELS else k
                    print(f"{label}: {v} tries")
        elif choice == "3":
            confirm = input("Type 'YES' to clear all scores: ").strip().upper()
            if confirm == "YES":
                best.clear()
                save_scores(best)
                print("Scores reset.")
            else:
                print("Cancelled.")
        elif choice == "4":
            break
        else:
            print("Try 1/2/3/4.")

if __name__ == "__main__":
    main_menu()
