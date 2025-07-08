from random import choice

# Initial Work

word_bank = {
    "Fruits": ["apple", "banana", "cherry", "mango"],
    "Animals": ["cat", "dog", "elephant", "lion"],
    "Countries": ["India", "Brazil", "France", "Japan"],
}

# Game Setting: Word Selection
# Ask the user for what category they want to pick (show the available categories).
"""
Current Categories:
	1. Fruits
	2. Animals
	3. Countries

Choose a category: user input
"""

# Next, select a random word in the category (don't forget to import random)
user_input = None
possible_words = word_bank[user_input]
word = choice(possible_words)

# Actual Game: Letter Guessing
"""
Show the selected word as underscores
_____

Ask the user for a letter input.
Enter letter: "p"

If one of the letters of the word is in the selected word, reveal it
_pp__

While user has not guessed all the letter, keep asking for input. 
"""