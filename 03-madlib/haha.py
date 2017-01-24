print "Hello, this is a mad lib script generator. Please fill out the questions below:"

def input(kind):
	response = raw_input("{}: ".format(kind))
	if response == "":
		print "Please enter something"
		response = input(kind)
	else:
		return response

noun1 = input("noun")
noun2 = input("noun")
verb1 = input("verb")
verb2 = input("verb")
adj1  = input("adjective")
adj2  = input("adjective")
adv1  = input("adverb")
adv2  = input("adverb")

print "Here goes nothing..."
print "The very {0} {1} {2} {3} through the kitchen.".format(adj1, noun2, verb1, adv2)
print "And then, the overly {0} {1} {2} {3} in the yard.".format(adj2, noun1, verb2, adv1)
