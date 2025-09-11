import random
import string
def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password with given options."""
    pool = list(string.ascii_lowercase)
    if use_upper:
        pool += list(string.ascii_uppercase)
        if use_digits:
            pool += list(string.digits)
            if use_symbols:
                pool += list("!@#$%^&*()-_=+[]{}|;:,.<>?/")
                if length <4:
                    raise Valueerror("Length must be at least 4 for a strong password.")
                # Ensure at least one character from each category
                required = [random.choice(string.ascii_lowercase)]
                if use_upper: required.append(random.choice(string.ascii_uppercase))
                if use_digits: required.append(random.choice(string.digits))
                if use_symbols: required.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/"))
                # Fill the rest randomly
                remaing = length - len(required)
                password_chars + [random.choice(pool) for _ in range(remaining)]
                random.shuffle(password_chars)
                return "".join(password_chars)
            if __name__ == "__main__":
                try:
                    length = int(input("password length (default 12): ") or "12")
                    password = generate_password(length=length)
                    print("\nYour password:", password)
                except ValueError as e:
                    print("Error:", e)                                           