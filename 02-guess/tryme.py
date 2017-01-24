import random

# Set difficulty
def mode():
    difficulty = raw_input("What level of difficulty would you like: Easy (1-10, 5 guesses) or hard (1-100, 10 guesses)?\n")
    # Clean user input
    difficulty = difficulty.lower()
    # If input is clean return
    if (difficulty == "easy") or (difficulty == "hard"):
        return difficulty
    # Otherwise, enter recursion
    else:
        print "Sorry, that doesn't compute."
        difficulty = mode()

# Get single random number
def getrand(low,high):
    # Generate whole number between values given
    return random.randint(low,high)

# Get guess from user
def guess():
    user = raw_input("What is your guess?\n")
    # Try to set user guess to int (will fail if words or null or non-int number)
    try:
        user = int(user)
        return user
    # If it fails, enter recursion
    except:
        print "That's not a whole number, try again.\n"
        user = guess()

# Check to see if guess is correct
def check(gue,num):
    # If the guess is too high, say so
    if gue > num:
        print "Your guess is too high.\n"
        keepgoing = True # Game continues
    # If the guess is too low, say so
    elif gue < num:
        print "Your guess is too low.\n"
        keepgoing = True # Game continues
    # If the guess is correct, say so
    else:
        print "That's right!"
        keepgoing = False # Game ends
    return keepgoing

# ------------------------------------------------------------------------------------------------------------------

# Begin game
print "Let's play a game. I'll think of a number and you try and guess it."

# Set vars
play = True
# Initialize global vars with easy default
lownum = 1
highnum = 10
guesses = 5

# Get difficulty
difficulty = mode()

# Change vars if hard
if difficulty == "hard":
    lownum = 1
    highnum = 100
    guesses = 10

# Get random number in given range
randnum = getrand(lownum,highnum)

print "Great, let's play."

# While the game should continue
while play == True:
    # Check for plurality of guesses
    if guesses > 1:
        print "You have {} guesses left".format(guesses)
    else:
        print "Last guess!"
    
    #print "Solution: {}".format(randnum) # For testing
    
    # Get guess 
    guessnum = guess()

    # Check guess, if they won play will be False and the game will end (exit loop)
    play = check(guessnum, randnum)

    # Remove one guess from guess count
    guesses = guesses - 1

    # If user is out of guesses, set play to False and end the game (exit loop)
    if guesses == 0:
        play = False

# Check to see if they were out of guesses, if so then they lost
if guesses == 0:
    print "You lost" # Future feature: Add play again?
# If they still have guesses left and the game ended then they won!
elif guesses > 0:
    print "You win!"

print "Thanks for playing!"
