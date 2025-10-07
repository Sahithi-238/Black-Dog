import random
import string

def generate_password(length=12):
    """Generate a random password containing letters, digits, and symbols."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable sequences
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password(12))
