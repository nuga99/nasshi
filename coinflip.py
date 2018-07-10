# Here is the 3rd challenge for Chapter 3 in 'Python Programming for the Absolute Beginner"
# Muhammad Hadi, 10th of July 2018
# If there's anything the same between mine of other(s), I'm terribly sorry.

import random
heads_n = 0
tails_n = 0
count = -1

print("\tWelcome to the flipping coin experience!\n")
print\
           ("""
Here you'll do some flipping for fun. Here is a challenge I should do to fullfill
my duty in "Python Programming for the Absolte Beginner" Chapter 3. This program will automatically
flip your coin, no matter how many number you put.

I feel dumb.
            """)

kambing = int(input("Press enter to flip a coin. How many times do you wanna flip?: "))

while True:
    babi = random.randint(0,1)
    count+=1
    if count == kambing:
        break
    
    elif babi == 1:
        print("heads")
        heads_n += 1
        
    elif babi == 0:
        print("tails")
        tails_n += 1

print("you did", heads_n,"heads and",tails_n,"tails in", count,"turns!")

input("Press enter to exit the program.")
