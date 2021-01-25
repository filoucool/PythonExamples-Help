import random
min = 1
max = 6

roll_again = "yes" #by default

if roll_again == "no":
    sys.exit(0)
while roll_again == "yes":
    print "Rolling the dice..."
    print random.randint(min, max)
    roll_again = raw_input("Roll again? Yes or no")