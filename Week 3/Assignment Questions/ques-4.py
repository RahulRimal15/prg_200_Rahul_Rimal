passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_characters = "!@#$%^&*"

for password in passwords:
    print("\nPassword:", password)

    missing = []

    if len(password) < 8:
        missing.append("Minimum 8 characters")

    if not any(ch.isupper() for ch in password):
        missing.append("Uppercase letter")

    # by Rahul Rimal

    if not any(ch.islower() for ch in password):
        missing.append("Lowercase letter")

    if not any(ch.isdigit() for ch in password):
        missing.append("Digit")

    if not any(ch in special_characters for ch in password):
        missing.append("Special character")

    if len(missing) == 0:
        print("Strong Password")
    else:
        print("Weak Password")
        print("Missing:", ", ".join(missing))