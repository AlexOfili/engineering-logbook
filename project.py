# Tip Splitter
def split_tip(bill, tip_percent, people):
    """Work out what each person owes, including tip."""
    total = bill * (1 + tip_percent / 100)
    return round(total / people, 2)

print(split_tip(100, 15, 4))  # Example usage