"""Bagels, by Al Sweigart al@inventpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is feature in this book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3 #Max digits
MAX_GUESSES = 10 #Number of guesses

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
    ''')