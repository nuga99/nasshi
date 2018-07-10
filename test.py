import time
import sys

# Guess My Number Game. Of course, with StackOverflow help. :(
# Challenge #3, Chapter 3, Python for Absolute Beginner
# Muhammad Hadi, 10th of July 2018

import random
import sys #system module in python
import time #time module python


jumlah = 0

print("\t\t\t\tWelcome to \'Guess My Number Game\'!\n")
print\
        ("""
Here is a game where you should guess what my number is. 
please kill me.
The number will be between 1-100!
        """)

angka = random.randrange(100) + 1
count_down=5
bangsat = int(input("Please input your first guessing here: "))

while (bangsat != angka and count_down>0):
    if bangsat > angka:
        time.sleep(1)
        count_down -= 1
        print("Whoa, youre a bit over!")
        jumlah +=1
        
        if(count_down==0):
            print("Game Over Too Slow")
            sys.exit()
    else:
        print("Hmm, youre a bit too low.")
        time.sleep(1)
        count_down -= 1
        jumlah +=1

        if(count_down==0):
            print("Game Over Too Slow")
            sys.exit()
            
    bangsat = int(input("Enter your next guessing here: "))

# you can also put 'jumlah +=1' after 'bangsat'.
    
print("wow, you did it! The number is",angka,"!. FYI, you did it in", jumlah,"moves. Meh.")

input("\n\nPress enter to exit, goblok.")


'''
boom = int(input("Countdown form:"))
while boom > 0:
    time.sleep(1)
    print(boom)
    boom -= 1

if(boom==0): sys.exit()
'''
