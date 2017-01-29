import csv, random

winner = False

# Get words
def getwords():
    # Set var to dict
    words = {}
    # Crack open CSV data
    csvfile = open('words.csv', 'r')
    # Reads the CSV, see: https://docs.python.org/2/library/csv.html#csv.DictReader
    reader = csv.DictReader(csvfile)
    # Loop over each row of the CSV
    for row in reader:
        #print "id: {0}, word: {1}".format(row['id'], row['word'])
        wordID = row['id']
        word = row['word']
        words[wordID] = word
    return words

# Get single random number
def getrand(low,high):
    # Generate whole number between values given
    return random.randint(low,high)

def guess():
    letter = raw_input('What letter do you guess?\n> ')
    # Clean input
    letter = letter.lower()
    # If more than one letter, throw error, enter recursion
    if len(letter) > 1:
        print "One single letter please."
        guess()
    return letter

def check(guess):
    # Loop over letters in game (the remaining letters)
    for i, l in enumerate(game):
        # If the guess is correct
        if l == guess:
            # Pop the guess out of game to remove it from possible guesses
            game.pop(i)

def giveClues(guess,letters,clue):
    # Convert clue to list
    clue = list(clue)
    # Loop over letters in letters (all letters in word)
    for i, l in enumerate(letters):
        # If the guess is in there
        if l == guess:
            # Add letter into the clue
            clue[i] = l
    # Convert clue back to string
    clue = "".join(clue)
    return clue

# Get fifty of the most used words
data = getwords()
# Select random number between 1 and 50
rand = getrand(1, len(data))
# Get random word
word = data[str(rand)]
# override for testing
word = 'testing'

# Creat list out of characters in word string
letters = list(word)
# Count the number of elements in that list (letters in the word)
count = len(letters)

# Set up clue variable, starting with all underscores 
clue = "_" * count
print "Your word is {0} letters long.\nHere it is: {1}".format(count,clue)

# Make copy of letters list to keep track of user's progress
# See: http://stackoverflow.com/a/21983106
game = letters[:]

# Set up how many guesses the user gets, this is generous
play = 15
if count > 5:
    play = 20 

# Start game loop
# While ...
# ... there are still letters left to guess AND ...
# ... there are still guesses left
while len(game) and play > 0:
    # Print out stuff
    print "\n\n\n"
    print "-------------------------------"
    print "\nYour word: {0}".format(clue)
    print "You have {0} guesses left.".format(play)
    
    # Get user guess
    userInput = guess()
    # Check guess
    check(userInput)
    # Get clue for user, compare guess to letters, then modify clue
    clue = giveClues(userInput,letters,clue)
    # Countdown for guesses left
    play = play - 1

# Game over
if play > 0:
    print "\n\nYou win!\nThe word was: {0}".format(word)
else:
    print "\n\nI'm sorry, you lost.\nThe word was: {0}".format(word)




