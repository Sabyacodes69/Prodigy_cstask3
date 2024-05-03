import re

def check_password_strength(password):
    # Criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    digit_weight = 1
    special_char_weight = 3

    # Initialize score
    score = 0

    # Check length
    if len(password) >= 8:
        score += length_weight

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += uppercase_weight

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += lowercase_weight

    # Check for digits
    if re.search(r'\d', password):
        score += digit_weight

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?`~|\\]', password):
        score += special_char_weight

    return score

def assess_password_strength(password):
    score = check_password_strength(password)

    if score >= 10:
        return "Strong"
    elif score >= 6:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
