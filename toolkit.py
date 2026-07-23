# Tip Splitter
def split_tip(bill, tip_percent, people):
    """Work out what each person owes, including tip."""
    total = bill * (1 + tip_percent / 100)
    return round(total / people, 2)

print(split_tip(100, 15, 4))  # Example usage



#Unit Converter
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


print("Converted length:", convert_length(100, 'meters', 'feet'))  # Example conversion

