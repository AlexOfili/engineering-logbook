import random


# Tip Splitter
def split_tip(bill, tip_percent, people):
    """Work out what each person owes, including tip."""
    total = bill * (1 + tip_percent / 100)
    return round(total / people, 2)


# Unit Converter
def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another."""
    conversion_factors = {
        'meters': 1,
        'centimeters': 100,
        'millimeters': 1000,
        'kilometers': 0.001,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        'miles': 0.000621371
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid units provided.")

    # Convert from the original unit to meters
    value_in_meters = value / conversion_factors[from_unit]

    # Convert from meters to the target unit
    converted_value = value_in_meters * conversion_factors[to_unit]

    return converted_value


# Basket total with discount
def basket_total(prices, discount=0.0):
    """Add up a list of prices, then apply a discount."""
    subtotal = sum(prices)
    return round(subtotal * (1 - discount), 2)


# Password Strength Checker
def password_strength(password):
    """Return 'weak', 'medium', or 'strong'."""
    length_ok = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)

    score = sum([length_ok, has_digit, has_upper])

    if score == 3:
        return "strong"
    elif score == 2:
        return "medium"
    else:
        return "weak"


# Number Guessing Game
def guessing_game(max_number=20):
    """Let the player guess a random number."""
    secret = random.randint(1, max_number)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_number}: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess == secret:
            print(f"Correct! It took you {attempts} attempts.")
            break
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")


if __name__ == "__main__":
    print(split_tip(100, 15, 4))  # Example usage
    print("Converted length:", convert_length(100, 'meters', 'feet'))  # Example conversion
    print("Basket total:", basket_total([1.35, 2.20, 0.99], discount=0.1))  # example total with discount
    user_password = input("Enter a password to check: ")
    print("Password strength:", password_strength(user_password))
    guessing_game()