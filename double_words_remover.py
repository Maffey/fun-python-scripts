import sys
import re
import os

def remove_double_words(file_path):
    """
    Reads a text file, removes consecutive identical words (case-insensitive),
    and saves the changes back to the same file.

    Args:
        file_path (str): The path to the text file to process.
    """
    try:
        # --- Read the file content ---
        # Use utf-8 encoding for broader compatibility
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # --- Find and remove double words using regex ---
        # \b      - Matches a word boundary to ensure we match whole words
        # (\w+)   - Matches one or more word characters (letters, numbers, underscore)
        #           and captures it in group 1.
        # \s+     - Matches one or more whitespace characters (space, tab, newline)
        # \1      - Backreference to the exact text matched by the first capturing group (the word)
        # \b      - Matches another word boundary
        # re.IGNORECASE - Makes the matching case-insensitive
        # The replacement pattern r'\1' replaces the entire match (e.g., "the the")
        # with just the first captured word (e.g., "the").
        # We use a loop with re.sub because a simple sub might miss overlaps like "the the the"
        # (it would replace the first "the the", leaving "the the").
        processed_content = original_content
        # Keep applying the substitution until no more changes are made
        while True:
            new_content = re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', processed_content, flags=re.IGNORECASE)
            if new_content == processed_content: # No more changes, break the loop
                break
            processed_content = new_content # Update content for the next iteration


        # --- Check if any changes were made ---
        if processed_content == original_content:
            print(f"No consecutive double words found in '{file_path}'. File unchanged.")
            return True # Indicate success (no changes needed)

        # --- Write the modified content back to the file ---
        # Open in write mode ('w'), which overwrites the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)

        print(f"Successfully removed double words and saved changes to '{file_path}'.")
        return True # Indicate success

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return False # Indicate failure
    except IOError as e:
        print(f"Error reading or writing file '{file_path}': {e}")
        return False # Indicate failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False # Indicate failure

def main():
    """
    Main function to handle command-line arguments.
    """
    # Check if a file path argument is provided
    if len(sys.argv) != 2:
        print("Usage: python double_words_remover.py <path_to_text_file>")
        sys.exit(1) # Exit with an error code

    file_path = sys.argv[1]

    # Check if the provided path is actually a file
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file or does not exist.")
        sys.exit(1)

    # Process the file
    if not remove_double_words(file_path):
        sys.exit(1) # Exit with an error code if processing failed

if __name__ == "__main__":
    main()