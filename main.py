#!/usr/bin/python
import random # used to generate random word from the words list

#import array as arr
"""This will be my hangman program that I am making"""

"""what do I need
-command prompt
-loop untill the end of the game
-array with the word to guess
-constant with the fixed amount of guesses
-loop(search) through the array of the given word with any guessed letters.
-print the head, left/right arms, middle body, left/right legs
-add word to a stack and remove letters from the stack once correctly guessed


command can use click? try normal at first
loop while guesses under

 ()
____
 !!
 /\


"""
#ALLOWED_GUESS = 6

#num_correct_guesses = 0
num_wrong_guesses = 0
"""get the users guess"""
def user_guess():
    cur_guess = raw_input("guess a letter: ")
    if not cur_guess.isalpha() or len(cur_guess) != 1:
        print("that is not an alphbetic character, or it is not exactly one character. Please try again")
    return cur_guess

"""check if the current guess has been used in this round already"""
"""
def already_guessed(guess, stack):
    if stack.find(guess) > -1: # if the guessed letter is in the word it will be a positive number
        print("You have already guessed that letter")
        add_wrong_guess()
"""

"""function to find the current wrong number of guesses"""
def add_wrong_guess():
    global num_wrong_guesses
    num_wrong_guesses += 1
    #return num_wrong_guesses


"""check if the current guessed character in the current word"""
def cur_guess_status(guess, cur_word):
    if cur_word.find(guess) > -1: # if the guessed letter is in the word it will be a positive number
        print("yess")
    elif():                         # if it is -1 then the guessed letter is not in the word
        print("try again")
        add_wrong_guess()


"""Manage the word stack against the guessed letters"""
#def update_stack(guess, cur_word):
    #cur_stack = list(cur_word) # initialize the stack with the word to guess

    #if guess in cur_stack:
        #cur_stack.
        ## check the letter agains the stac

""" initiate the stack with each letter of the current word replace with underscores"""
def init_stack(word):
    cur_stack = list(word) # initialize the stack with the word to guess as a list
    blank = "_"

    for i in range(len(cur_stack)) :
        cur_stack[i] = "_"
    #print(' '.join(cur_stack))


    return (''.join(cur_stack))
"""This functioin compares the original word to the current stack to see if they are the same and returns ture if they are the same"""
def check_win(orig_word, stack_word):
    if orig_word == stack_word:
        return True
    else:
        return False


""" #this function will print out the current correctly guessed letters of the word."""
def build_word(current_word, word_stack, guess_char):
    """
    create a string with the same mumber of characters as the word to guess
    change the letters to underscores for each character
    update each character as they are guessed correctly and print the updated word after each correct guess
    """
    #global cur_word   #current chosen word
    local_word = current_word # assign local var with current word as a list
    #global word_stack
    #global cur_stack
    #cur_stack = list(cur_word) # initialize the stack with the word to guess as a list
    for place in range(len(local_word)) :
        if guess_char == local_word[place]:
            word_stack[place] = guess_char
            print("localword is", local_word[place])
            print("the guessed character is", guess_char)
            print("the wordstack is", word_stack[place])
    #print(' '.join(cur_stack))
    print(guess_char, word_stack[place])

    fword_state = (''.join(word_stack))


    return fword_state

def draw_hangman():
    hangman = ""
    global num_wrong_guesses
    if num_wrong_guesses == 1:
        hangman = ('''
           ____
           |  |
           |  O
              ''')
    elif num_wrong_guesses == 2:
        hangman = ('''
           ____
           |  |
           |  O
              |
              ''')
    elif num_wrong_guesses == 3:
        hangman = ('''
           ____
           |  |
           |  O
              |\\
              ''')
    elif num_wrong_guesses == 4:
        hangman = ('''
           ____
           |  |
           |  O
             /|\\
              ''')
    elif num_wrong_guesses == 5:
        hangman = ('''
           ____
           |  |
           |  O
             /|\\
               \\

              ''')
    elif num_wrong_guesses == 6:
        hangman = ('''
           ____
           |  |
           |  O
             /|\\
             / \\

              ''')
    #return ("the number of wrong guesses are ", num_wrong_guesses)
    return hangman

def main():
    DICIONARY = ("python", "aligator", "lizard", "mouse")
    cur_word = random.choice(DICIONARY)
    global num_wrong_guesses
    num_wrong_guesses = 0
    #guess_number
    global cur_stack
    current_stack = init_stack(cur_word) # initiate the stack with each letter of the current word replace with underscores
    #print(current_stack)
    ncurrent_stack = list(current_stack)
    print ("The current word is ", current_stack) # this is doing what it should be doing, what is the current stack


    guess_number = 0 # the current number of guess
    while num_wrong_guesses < 6:
        my_guess = user_guess()
        stack = (build_word(cur_word, ncurrent_stack, my_guess))
        check_winner = check_win(cur_word, stack)
        if check_winner is True:
            print("You Won, Sweeeeeeet!!!!!!!!!")
            quit()
        guess_number += 1
        print("\n\n\n")
        print("your current guess is, ", my_guess)

        if num_wrong_guesses < 6:
             cur_guess_status(my_guess, cur_word)
            # already_guessed(my_guess, stack)
        else:
            print("===========================================")
        print(list(stack), " = ", list(cur_word))

        #draw the current state of the hangman
#        print(draw_hangman())

        print(guess_number, "tries") #how man wrong guesses so far
        print("\n")
    print("Game over")


if __name__ == "__main__":
    main()
