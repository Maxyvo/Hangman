# Name: Hangman
# Author: Maxime Yvonet
# Date Created: November 22, 2022
# Date Last Modified: December 9, 2022
# Purpose: To guess a random word by inputting letters with a maximum of 6 wrong guesses
#----------------------------------------------------------------------------------------
# Conestoga College - PROG1783 Final project

import random

# Empty word list
word_list = []

def import_words():
    # Open word txt file and read
    words = open("words.txt", "r")
    # Append every word from the word txt file to the empty word lis
    for i in words:
        word_list.append(i.strip())
    # Close file
    words.close()

# Choose a random word from the list
def get_word():
    word = random.choice(word_list)
    return word

def enter_letter():
    while True:
        # Ask user to guess a letter
        guess = input("Please guess a letter: ")
        # Check if the guess is a letter and has a length of 1
        if len(guess) == 1 and guess.isalpha():
            # Convert to lower case
            return guess.lower()
        # Ask user to guess again if guess is not a letter or is length is longer than 1
        print("Must be a letter")

def print_guessed(guessed_letters, word):
    # Counter of unknown letters
    unknown = 0
    for c in word:
        # Check if the guessed letter matches one of the letters in the word
        if c in guessed_letters:
            # Reveals the guessed letter at the exact position if one of the guessed letters has a match
            print(c, end="")
        else:
            # Increment unknown by 1
            unknown += 1
            # Keeps the word unknown by replacing the letter with "_" if the guessed letters does not match
            print("_", end="")
    print("\n")
    return unknown


def game(word):
    # Empty list for guessed letters
    guessed_letters = []
    # Counter for number of wrong guesses
    fails = 0

    # Loop until the number of wrong guesses reaches 6
    while fails < 6:
        guess = enter_letter()
        print(guess)
        # Check for duplicate letters in the guessed letters list
        if guess in guessed_letters:
            # Display guessed letters list
            print(guessed_letters)
            # Let user know if that letter has already been guessed
            print("Already tried")
            # Let user try again
            continue
        else:
            # Add guessed letter to the list if it's not a duplicate
            guessed_letters.append(guess)
            # Display guessed letters list with the added guessed letters
            print(guessed_letters)
        # Check if guessed letter is wrong
        if not guess in word:
            # Adds 1 to the wrong guess counter
            fails +=1
            # Display the drawing for every time the letter is wrong
            hangman(fails)

        # Print the word with "_" as unknown letters and count the number of unknowns
        unknown = print_guessed(guessed_letters, word)
        # Check all unknown letter is found
        if unknown == 0:
            # Display that the user wins
            print("You win!")
            # Ends the game
            break

    # Check if the number of wrong guesses reaches 6
    if fails == 6:
        # Display that the user loses
        print("You lose!")
    # Reveals what the word was
    print("The word was", word)

# 6 drawings for the wrong guessed letters
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
    # Display the drawings for the number of wrong guesses
    print(failed[fails])

# Main game
def play():
    # Welcome screen display for user
    print("Welcome to hangman\n")
    while True:
        # Call function to populate word list
        import_words()
        # Pick a word randomly from the list
        word = get_word()
        # Print word with empty guesses
        print("_" * len(word))
        # Call function for guessed letters list and wrong guesses counter
        game(word)
        # Ask user if they want to play again
        print("Do you want to play again? ")
        # Ask user to choose an option between yes or no
        play_again = input("Enter 'y' for yes and 'n' for no: ")
        # Check if the play again is not yes
        if play_again != "y":
            # Ends the game
            break
        # Line space for a new game
        print("\n")

play()

