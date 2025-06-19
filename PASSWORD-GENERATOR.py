import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4.")
        return ""

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one character from each set
    all_chars = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    pwd = generate_password(length)
    print("Generated Password:", pwd)
