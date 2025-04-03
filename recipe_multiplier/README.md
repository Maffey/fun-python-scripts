# Recipe Calories Multiplier

A simple Python tool that helps you scale recipe ingredients by a multiplier of your choice.

## Is AI taking our jobs?

This project (including the README.md here, except this paragraph) was completely done by AI and the premium version of Cursor.
I've only provided the prompts.
It was a fun experience watching the AI agent struggle. In the end, the script does kinda work and handles the usual cases,
but it was completely defeated by fractions, and multiple retries at solving the problem yielded similar problems.

Essentially, this:

```text
- 1 Tablespoon dark soy sauce
- 1 1/2 Tablespoons vegetable oil
- 1/2 yellow onion, thinly sliced
```

multiplied by 2, yielded this:

```text
- 2 Tablespoon dark soy sauce
- 3 Tablespoons vegetable oil
- 2/4 yellow onion, thinly sliced
```

and the agent couldn't get over the regular, basic fractions, despite knowing how to handle basic fractions.

Moral is simple - it's a powerful tool that can do a lot in a short time,
but there will be always a developer needed to guide the agent and fix its mistakes.

And the bigger the project, the worse the AI works.

Overall, great for Proof of Concepts and materializing simple ideas.

## Features

- Supports both comma and period decimal separators (e.g., 1.5 and 1,5)
- Handles numbers with spaces (e.g., "1 000" becomes "1000")
- Works on both Windows and Linux
- Opens a text editor for easy recipe input
- Rounds results to one decimal place

## Requirements

- Python 3.x
- A text editor (on Windows: Notepad, on Linux: xdg-open, gedit, or nano)

## Usage

1. Run the script:
   ```bash
   python recipe_multiplier.py
   ```

2. Enter the multiplier value when prompted (e.g., 2.0)
3. A text editor will open. Paste your recipe and save/close the editor.
4. The program will display the scaled recipe with all numbers multiplied by your chosen value.

## Example

Input recipe:

```
400 g chicken, 0.5  liters of water, 8 g sugar
```

With multiplier 2, output will be:

```
800 g chicken, 1 liters of water, 16 g sugar
``` 