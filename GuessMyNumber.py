# Guess My Number Game. Of course, with StackOverflow help. :(
# Challenge #3, Chapter 3, Python for Absolute Beginner
# Muhammad Hadi, 10th of July 2018

import random
jumlah = 0

print("\t\t\t\tWelcome to \'Guess My Number Game\'!\n")
print\
        ("""
Here is a game where you should guess what my number is. 

please kill me.

The number will be between 1-100!
        """)

angka = random.randrange(100) + 1

bangsat = int(input("Please input your first guessing here: "))

while bangsat != angka:
    if bangsat > angka:
        print("Whoa, youre a bit over!")
        jumlah +=1
    else:
        print("Hmm, youre a bit too low.")
        jumlah +=1
    bangsat = int(input("Enter your next guessing here: "))

# you can also put 'jumlah +=1' after 'bangsat'.
    
print("wow, you did it! The number is",angka,"!. FYI, you did it in", jumlah,"moves. Meh.")

input("\n\nPress enter to exit, goblok.")


