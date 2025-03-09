import re

# List of common weak passwords
COMMON_PASSWORDS = ["123456", "password", "123456789", "12345", "12345678", "qwerty", "1234567", "111111", "123123", "abc123", "password1", "passw0rd", "admin", "letmein", "welcome", "iloveyou", "football", "monkey", "sunshine", "1234", "superman", "batman", "dragon", "shadow", "master", "qwertyuiop", "asdfghjkl", "zxcvbnm", "1q2w3e4r", "qazwsx"]

def check_password_strength(password):
    """Evaluates the strength of a given password and provides feedback."""
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Check numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:'\",.<>?/]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., !@#$%^&*).")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        strength = 0
        feedback = ["❌ This password is too common. Choose a more secure one."]

    # Determine password strength level
    if strength == 5:
        return "✅ Strong Password! 👍", feedback
    elif 3 <= strength < 5:
        return "⚠️ Moderate Password. Improve it!", feedback
    else:
        return "❌ Weak Password. Change it!", feedback


if __name__ == "__main__":
    password = input("Enter your password: ")
    result, suggestions = check_password_strength(password)
    print("\n" + result)
    for suggestion in suggestions:
        print(suggestion)
