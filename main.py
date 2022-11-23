# Name: Hangman
# Author: Maxime Yvonet
# Date Created: November 22, 2022
# Date Last Modified: November 23, 2022
# Purpose: To guess a random word by inputting letters with a maximum of 6 tries

import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word

def enter_letter():
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            # Convert to lower case
            return guess.lower()
        print("Must be a letter")

def print_guessed(guessed_letters, word):
    unknown = 0
    for c in word:
        if c in guessed_letters:
            print(c, end="")
        else:
            unknown += 1
            print("_", end="")
    print("\n")
    return unknown


def game(word):
    guessed = False
    guessed_letters = []
    fails = 0
    print("Welcome to hangman")
    print("\n")

    while fails < 6:
        guess = enter_letter()
        print(guess)
        if guess in guessed_letters:
            print("Already tried")
            continue
        else:
            guessed_letters.append(guess)
            print(guessed_letters)
        if guess in word:
            print("yes")
        else:
            print("no")
            fails +=1
            hangman(fails)

        unknown = print_guessed(guessed_letters, word)
        if unknown == 0:
            print("You win!")
            break


def hangman(fails):
    failed = ["""
             _____ 
           |    |  
           |    |  
           |      
           |      
           |      
           |      
           __|__""","""
             _____ 
           |    |  
           |    O
           |
           |      
           |      
           |      
           __|__""","""
             _____ 
           |    |  
           |    O
           |    |
           |    | 
           |      
           |      
           __|__""","""
             _____ 
           |    |  
           |    O
           |    |/
           |    | 
           |      
           |      
           __|__""","""
             _____ 
           |    |  
           |    O
           |   \\|/
           |    | 
           |      
           |      
           __|__""","""
             _____ 
           |    |  
           |    O
           |   \\|/
           |    | 
           |     \\ 
           |      
           __|__""","""
             _____ 
           |    |  
           |    O
           |   \\|/
           |    | 
           |   / \\ 
           |      
           __|__"""]
    print(failed[fails])

def test():
    word = get_word()

    #Debugging code
    print("Word to guess is ", word)

    game(word)

test()

