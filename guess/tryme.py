import random

# Need to clean this up
print "Let's play a game. I'll think of a number and you try and guess it."
lownum = int(raw_input("What should the lowest number in the range be?"))
highnum = int(raw_input("What should the highest number in the range be?"))
print "Great, let's play."
# Need to add language where if range is greater than 100, I warn users it's going to be very hard for them

# Get random number
def getrand(low,high):
    # Generate whole number between 1 and 6
    return random.randint(low,high)

def guess():
    user = raw_input("What is your guess?\n")
    user = int(user)
    if type(user) is not int:
        print "That's not a whole number, try again.\n"
        user = guess()
    return user

def check(gue,num):
    if gue > num:
        print "Your guess is too high, try again\n"
        keepgoing = True
    elif gue < num:
        print "Your guess is too low, try again\n"
        keepgoing = True
    else:
        print "That's right!\n"
        keepgoing = False
    return keepgoing

# Need to keep track of turns, how many guesses should they get?
# Maybe an easy, medium, hard and insane levels with set ranges and amount of guesses?

# Set vars
play = True
randnum = getrand(lownum,highnum)

while play == True:
    #print randnum # For testing
    guessnum = guess()
    #print guessnum # For testing
    play = check(guessnum, randnum)

print "Thanks for playing!"

