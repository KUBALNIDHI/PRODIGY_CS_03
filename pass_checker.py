import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    # Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Number Check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Final Strength Feedback
    if strength == 4:
        return "Password Strength: Strong", feedback
    elif strength == 3:
        return "Password Strength: Medium", feedback
    else:
        return "Password Strength: Weak", feedback

print(" Password Complexity Checker")
user_password = input("Enter your password: ")
result, tips = check_password_strength(user_password)

print("\n" + result)
if tips:
    print("\nSuggestions:")
    for tip in tips:
        print("-", tip)
