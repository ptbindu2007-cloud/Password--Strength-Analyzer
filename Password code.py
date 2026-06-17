import re

def analyze_password_strength(password):
    """
    Analyzes the strength of a password based on common security criteria.
    """
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (use at least 8-12 characters).")

    # Criteria 2: Character Variety
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !@#$).")

    # Determine Rating
    if score >= 6:
        rating = "Very Strong"
    elif score >= 4:
        rating = "Strong"
    elif score >= 2:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

# Example Usage:
user_input = input("Enter a password to analyze: ")
rating, feedback = analyze_password_strength(user_input)

print(f"\nPassword Strength: {rating}")
if feedback:
    print("Suggestions to improve:")
    for tip in feedback:
        print(f"- {tip}")