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

def game(word):
    word_length = "_ " * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print("Welcome to hangman")
    #print(hangman(tries))
    print(word_length)
    print("\n")
    while True:
        guess = input("Please guess a letter: ")

'''def hangman(tries):
    tried = ["""
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
    return hangman[tried]
    '''

def test():
    word = get_word()
    game(word)

test()

