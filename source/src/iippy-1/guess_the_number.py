# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui


# helper function to start and restart the game
def new_game():
    global max_choose
    global i
    print "Choose a range to start your game Guess_the_number"
    max_choose = int(raw_input("Choose range 0 to 100 please input 100,range 0 to 1000 please input 1000:\n"))
    range_choose(max_choose)
    print "Good Job!"
    print "Guess a number in that range."
    if max_choose == 100:
        i = 7
    elif max_choose == 1000:
        i = 10
    input_guess(i)



# define event handlers for control panel
def range_choose(max_choose):
    global random_choose
    if max_choose == 100 or max_choose ==1000:
        random_choose = random.randrange(0, max_choose)
        print "You've choose the range 0 to %d" % max_choose
    else:
        print "I don't know what you're talking about..."
    
    return

def input_guess(i):
    if i > 1:
        guessed_number = int(raw_input("Please input your guess:\n"))
        print "You've guessed %d " % guessed_number
        print "You have %d chances to guess" % int(i-1)
        compare(guessed_number,i)
    else:
        print "You have no chances to guess"
    return
def compare(guessed_number,i):
    difference = guessed_number - random_choose
    if difference == 0:
        print "Correct while remains %d chances" % i
    elif difference < 0:
        print "Higher"
        i = i - 1
        input_guess(i)
    else:
        print "Lower"
        i = i - 1
        input_guess(i)
    return


# create frame

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math


# helper function to start and restart the game
def new_game():
    global max_choose
    global i
    print "Choose a range to start your game Guess_the_number"
    max_choose = int(raw_input("Choose range 0 to 100 please input 100,range 0 to 1000 please input 1000:\n"))
    range_choose(max_choose)
    print "Good Job!"
    print "Guess a number in that range."
    if max_choose == 100:
        i = 7
    elif max_choose == 1000:
        i = 10
    input_guess(i)



# define event handlers for control panel
def range_choose(max_choose):
    global random_choose
    if max_choose == 100 or max_choose ==1000:
        random_choose = random.randrange(0, max_choose)
        print "You've choose the range 0 to %d" % max_choose
    else:
        print "I don't know what you're talking about..."
    
    return

def input_guess(i):
    if i > 1:
        guessed_number = int(raw_input("Please input your guess:\n"))
        print "You've guessed %d " % guessed_number
        print "You have %d chances to guess" % int(i-1)
        compare(guessed_number,i)
    else:
        print "You have no chances to guess"
    return
def compare(guessed_number,i):
    difference = guessed_number - random_choose
    if difference == 0:
        print "Correct while remains %d chances" % i
    elif difference < 0:
        print "Higher"
        i = i - 1
        input_guess(i)
    else:
        print "Lower"
        i = i - 1
        input_guess(i)
    return


# create frame
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math


# helper function to start and restart the game
def new_game():
    global max_choose
    global i
    print "Choose a range to start your game Guess_the_number"
    max_choose = int(raw_input("Choose range 0 to 100 please input 100,range 0 to 1000 please input 1000:\n"))
    range_choose(max_choose)
    print "Good Job!"
    print "Guess a number in that range."
    if max_choose == 100:
        i = 7
    elif max_choose == 1000:
        i = 10
    input_guess(i)



# define event handlers for control panel
def range_choose(max_choose):
    global random_choose
    if max_choose == 100 or max_choose ==1000:
        random_choose = random.randrange(0, max_choose)
        print "You've choose the range 0 to %d" % max_choose
    else:
        print "I don't know what you're talking about..."
    
    return

def input_guess(i):
    if i > 1:
        guessed_number = int(raw_input("Please input your guess:\n"))
        print "You've guessed %d " % guessed_number
        print "You have %d chances to guess" % int(i-1)
        compare(guessed_number,i)
    else:
        print "You have no chances to guess"
    return
def compare(guessed_number,i):
    difference = guessed_number - random_choose
    if difference == 0:
        print "Correct while remains %d chances" % i
    elif difference < 0:
        print "Higher"
        i = i - 1
        input_guess(i)
    else:
        print "Lower"
        i = i - 1
        input_guess(i)
    return


# create frame
frame = simplegui.create_frame('Testing', 200, 200)
frame.add_input("Range: 0 - 1000",range_choose,100)
frame.add_input("", input_guess,50)
frame.add_button("Restart",new_game,100)

frame.start()

# register event handlers for control elements and start frame



new_game()









