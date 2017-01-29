def success():
    print "\n\nYou make it back to the locked door, use the key and open up the door.\nSuddenly you wake up in a cold sweat and realize you shouldn't watch movies before bed.\n\n"

def lab():
    print "\n\nYou slowly enter the Laboratory and make your way down the stairs.\nYou encounter a hunchbacked man named Igor who ignores you.\nYou realize that this is Dr. Frankenstein's lab.\nYou see him working over a table.\nYou walk over and ask if he is, in fact, Dr. Frankenstein.\nHe says hello and politely informs you that it's pronounced Frankensteen.\nYou ask if he has a key to the front door and he says that he does not.\nYou return to the hallway.\n\n"
    hallway()

def saloon():
    print "\n\nYou slowly enter the Saloon and witness a vaudeville brawl in full swing.\nYou see a man, unaffected by the mayhem sitting at the bar so you sit down next to him.\nHe introduces himself: 'My name is Jim, most people call me... Jim.'\nYou notice that his holsters are empty as he finishes a bottle of whiskey.\nYou ask him if he has a key to the front door and he says that he left all he had in Waco.\nYou return to the hallway.\n\n"
    hallway()

def factory():
    print "\n\nYou slowly enter the Factory and see a man wearing a purple suit and top hat,\nhobbling around with a cane.\nHe is not very old but wears scorn on his face.\nHe notices you and moves toward you with a heavy limp.\nAs he approaches, he removes his top hat.\nSuddenly his cane sticks into the ground\nbut he continues for another step, before barrel rolling, popping up and welcoming you to his chocolate factory.\nYou ask if he has a key to the front door and he replies: 'I'm sorry, all questions must be submitted in writing'.\nYou return to the hallway.\n\n"
    hallway()

def office():
    print "\n\nYou slowly enter the Gardener's office just in time to witness\na group of teenagers and a dog pull the mask off of a man pretending to be a monster.\n'Jinkies,' one of the girls says. 'It was the gardner the whole time!'\nThe gardner replies: 'And I would've gotten away with it to if it weren't for you meddling kids and that dog.'\nOn the table you notice the key so you grab it and show yourself out of the room.\n\n"
    success()

def hallway():
    print "\nThere are three doors along the hallway and one at the end.\nThe first door is labeled 'Laboratory'.\nThe second door is labeled 'Saloon'.\nThe third is labeled 'Factory'.\nThe door at the end of the hallway is labeled 'Gardener's office'"
    userInput = raw_input("Which door would you like to try? One, two, three or office?\n> ")
    inputList = userInput.split(" ")
    if "one" in inputList:
        lab()
    elif "two" in inputList:
        saloon()
    elif "three" in inputList:
        factory()
    elif "office" in inputList:
        office()
    else:
        print "I'm sorry that doesn't make sense."
        hallway()

def miley():
    print "\n\nYou open the door and this room is very dark. You cannot see anything. Suddenly, a scantly clad young woman swings in like a wrecking ball, busting the walls down, and you retreat to the room with the locked door.\n\n"
    begin()

def begin():
    print "There is a door behind you but it's locked and you need a key to open it.\nTo your right, there is a blank wall.\nDirectly in front of you there is a closed, unlocked door.\nTo your left there is a dark hallway."
    userInput = raw_input("How would you like to proceed? Open door or go into the hallway?\n> ")
    inputList = userInput.split(" ")
    if "door" in inputList:
        miley()
    elif "hallway" in inputList:
        print "\nYou enter the dark hallway. Suits of armor line the walls and you notice dog treats scattered on the floor."
        hallway()
    else:
        print "I'm sorry that doesn't make sense."
        begin()


# Begin game
print "You wake up in a room you've never been in before."
begin()
print "Thanks for playing!"