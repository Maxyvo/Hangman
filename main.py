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
    print(hangman(tries))
    print(word_length)
    print("\n")
    guess = input("Please guess a letter: ")


def hangman(tries):
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


