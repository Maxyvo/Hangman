# Name: Hangman
# Author: Maxime Yvonet
# Date Created: November 22, 2022
# Date Last Modified: December 9, 2022
# Purpose: To guess a random word by inputting letters with a maximum of 6 tries

import random

word_list = []
words = open("words.txt", "r")
def import_words():
    for i in words:
        word_list.append(i.strip())
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
    guessed_letters = []
    fails = 0

    while fails < 6:
        guess = enter_letter()
        print(guess)
        if guess in guessed_letters:
            print(guessed_letters)
            print("Already tried")
            continue
        else:
            guessed_letters.append(guess)
            print(guessed_letters)
        if not guess in word:
            #print("no")
            fails +=1
            hangman(fails)

        unknown = print_guessed(guessed_letters, word)
        if unknown == 0:
            print("You win!")
            break

    if fails == 6:
        print("You lose!")
    print("The word was", word)

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

def play():
    print("Welcome to hangman\n")
    while True:
        import_words()
        word = get_word()
        print("_" * len(word))

        #Debugging code
        #print("Word to guess is ", word)

        game(word)
        print("Do you want to play again? ")
        play_again = input("Enter 'y' for yes and 'n' for no: ")
        if play_again != "y":
            break
        print("\n")

play()

