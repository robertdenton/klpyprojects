import random

# Default vars
play = True # When program starts you want to play
results = [] # There are zero results to begin with and we want them as a list, they could also be formatted as text
askcount = 0 # Counter in case user does not respond correctly

# Get a single die
def single():
    # Generate whole number between 1 and 6
    return random.randint(1,6)

# Roll the dice
def roll():
    # Get first die
    one = single()
    # Get second die
    two = single()
    # Put them in a list
    results = [one,two]
    # Return the list
    return results

# Ask if user would like to roll again
def ask(counter):
    # Get user feedback
    # ... First ask (advanced)
    if counter == 0:
        again = raw_input("Roll again? (yes or no) \n")
    # ... Second ask
    elif counter == 1:
        again = raw_input("\nNo spaces please. Or was there a typo maybe?\nWould you like to roll again? (yes or no) \n")
    # ... More asks
    else:
        again = raw_input("\nOk, be serious.\nWould you like to roll again? (yes or no) \n")
    # Clean user feedback
    again = again.lower()
    # Play again conditional, control for different types of responses
    if again == "no" or again == "n":
        play = False
        return play
    elif again == "yes" or again == "y":
        play = True
        return play
    # Control for all responses
    else:
        # Increase counter on user fail
        counter += 1
        # Recursively ask if they don't answer correctly (advanced topic)
        play = ask(counter)
        return play

# Main while loop, evaluates to True on first run
while play == True:
    # Roll the dice, set return equal to new numbers var
    numbers = roll()
    # Print out the last roll (advanced string formatting)
    print "\nYou're roll: {0}".format(numbers)
    # Ask if user wants to play again, set return equal to play
    # ... if True, loop will continue
    # ... if False, loop will end
    play = ask(askcount)

# Thank user, this only called after loop has finished
print "\nThanks for playing!"

