# Guess My Number Game v2.0. Of course, with StackOverflow & other resources help. :(
# Challenge #3, Chapter 3, Python for Absolute Beginner
# This game includes time limit and limited amount of guessing.
# Muhammad Hadi, 10th of July 2018

import random
import time

jumlah = 0
mulai = time.time()
waktu_awal = time.ctime()

print("\t\t\t\tWelcome to \'Guess My Number Game\'!\n")
print("Current time: ", waktu_awal)
print\
        ("""
Here is a game where you should guess what my number is. You have limited amount of
guessing, which is 10 times and also a time limit which is 2 minutes.
please kill me.

The number will be between 1-100! Are you ready?
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
    if jumlah == 10:
        print("\nYou have run out of guesses. You suck dick!!!!! xDlol")
        break
        input("\nPress enter to exit, goblok.")
              
# you can also put 'jumlah +=1' after 'bangsat'.
              
else:
    print("\nWow, you did it! The number is",angka,"!. FYI, you did it in", jumlah,"moves. Meh.")

selese = time.time()-mulai

print("\nYou spent", float(selese),"seconds.")
input("\nPress enter to exit, goblok.")
    



