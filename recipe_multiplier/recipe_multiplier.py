import re
import subprocess
import sys
import tempfile
import os
from fractions import Fraction

def get_multiplier():
    while True:
        try:
            value = input("Enter the multiplier value (max 1 decimal place): ")
            # Replace comma with period for consistent parsing
            value = value.replace(',', '.')
            multiplier = float(value)
            # Round to 1 decimal place
            multiplier = round(multiplier, 1)
            return multiplier
        except ValueError:
            print("Please enter a valid number.")

def process_fraction(fraction_str, multiplier):
    """Process a fraction string and multiply it by the given multiplier.
    
    Args:
        fraction_str (str): The fraction to process (e.g., "1/2", "1 1/2")
        multiplier (float): The number to multiply by
        
    Returns:
        str: The processed fraction as a string
    """
    # Handle zero case
    if fraction_str == "0":
        return "0"
    
    # Split into whole number and fraction parts if it's a mixed number
    parts = fraction_str.split()
    whole = 0
    fraction_part = None
    
    if len(parts) > 1:
        # It's a mixed number (e.g., "1 1/2")
        whole = int(parts[0])
        fraction_part = parts[1]
    elif '/' in fraction_str:
        # It's just a fraction (e.g., "1/2")
        fraction_part = fraction_str
    else:
        # It's just a whole number
        return str(int(float(fraction_str) * multiplier))
    
    # Process the fraction part if it exists
    if fraction_part:
        numerator, denominator = map(int, fraction_part.split('/'))
        # Convert to improper fraction
        total_numerator = whole * denominator + numerator
        # Multiply by the multiplier
        result = Fraction(total_numerator, denominator) * Fraction(str(multiplier))
        
        # Convert back to mixed number if needed
        whole_result = result.numerator // result.denominator
        remainder = result.numerator % result.denominator
        
        if remainder == 0:
            return str(whole_result)
        elif whole_result == 0:
            return str(Fraction(remainder, result.denominator))
        else:
            return f"{whole_result} {Fraction(remainder, result.denominator)}"
    
    return str(int(whole * multiplier))

def format_result(result):
    # If it's a whole number, return it as an integer
    if result.is_integer():
        return str(int(result))
    
    # For decimal numbers, round to 1 decimal place
    return str(round(result, 1))

def open_text_editor():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
        temp_path = temp_file.name

    # Try to find an available text editor
    editors = ['xdg-open', 'gedit', 'kate', 'nano', 'vim', 'vi']
    editor = None
    
    for e in editors:
        if os.system(f'which {e} > /dev/null 2>&1') == 0:
            editor = e
            break
    
    if editor is None:
        print("Error: No suitable text editor found. Please install one of: xdg-open, gedit, nano, vim, vi, or kate")
        sys.exit(1)

    print(f"\nOpening {editor}...")
    print("Please paste your recipe, save the file, and close the editor when done.")
    
    # Open the text editor and wait for it to close
    try:
        if editor == 'xdg-open':
            # xdg-open might return immediately, so we need to wait for the actual editor
            subprocess.run([editor, temp_path], check=True)
            input("\nPress Enter after you have saved and closed the editor...")
        else:
            # For other editors, they typically block until closed
            subprocess.run([editor, temp_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error: Could not open {editor}. Please try another editor.")
        sys.exit(1)

    # Read the content after the editor is closed
    try:
        with open(temp_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: The temporary file was not found. Did you save the file?")
        sys.exit(1)

    # Clean up the temporary file
    try:
        os.unlink(temp_path)
    except OSError:
        pass  # Ignore errors when removing the temp file

    return content

def process_recipe(text, multiplier):
    # Regular expression to match:
    # 1. Mixed numbers with fractions (e.g., "1 1/2")
    # 2. Simple fractions (e.g., "1/2")
    # 3. Regular numbers with decimals
    pattern = r'(\d+(?:\s+\d+/\d+)?|\d+/\d+|\d+(?:[.,]\d+)?)'
    
    def multiply_match(match):
        number_str = match.group(1)
        try:
            # If it contains a fraction, use process_fraction
            if '/' in number_str:
                return process_fraction(number_str, multiplier)
            # Otherwise handle as regular number
            number_str = number_str.replace(',', '.')
            number = float(number_str)
            result = number * multiplier
            if result.is_integer():
                return str(int(result))
            return str(round(result, 1))
        except ValueError:
            return match.group(0)

    return re.sub(pattern, multiply_match, text)

def main():
    print("Welcome to Recipe Calories Multiplier!")
    print("This app will help you scale recipe ingredients by a multiplier of your choice.")
    
    multiplier = get_multiplier()
    print(f"\nMultiplier set to: {multiplier}")
    print("\nPlease paste your recipe into the text editor that will open.")
    print("After you're done, save and close the editor to continue.")
    
    recipe = open_text_editor()
    if not recipe.strip():
        print("No recipe was provided. Exiting...")
        return
    
    result = process_recipe(recipe, multiplier)
    print("\nProcessed recipe:")
    print(result)

if __name__ == "__main__":
    main() 