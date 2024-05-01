# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
San Diego College of Continuing Education (SDCCE) Student ID: 5550203278
COMP 661: Programming with Python II
Assignment: Module 3, Question 2
Description: This program counts and prints duplicate words in a sentence using a dictionary.
Treat uppercase and lowercase letters the same. Assume there is no punctuation in the sentence.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS.

def count_duplicate_words(input_text):
    """Counts and prints duplicate words in a sentence using a dictionary.

    Parameters:
        input_text (str): A sentence with no punctuation.

    """

    duplicate_words = {}
    # Iterate through words in input text after ensuring they are lower case and split using spaces as delimiters
    for word in input_text.lower().split():
        # If word is not in dictionary, add as a key w/ count of 1, otherwise increment count by 1
        duplicate_words[word] = duplicate_words.get(word, 0) + 1

    # Print header of formatted table
    print("WORD         COUNT")

    # Return items in duplicate_words dictionary as a list of (word, count) tuples sorted by word,
    # then iterate through each tuple in the list
    for word, count in sorted(duplicate_words.items()):
        # only print duplicates
        if count > 1:
            print(f"{word:14} {count}")

def main():
    # Clear terminal window text in Windows OS.
    os.system('cls')

    input_text = (
        "Peter Piper picked a peck of pickled peppers "
        "A peck of pickled peppers Peter Piper picked "
        "if Peter Piper picked a peck of pickled peppers "
        "Where is the peck of pickled peppers "
        "Peter Piper picked"
    )

    # Count and display the duplicate words in input_text
    count_duplicate_words(input_text)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()
