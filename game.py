'''
Author : Amjad
Date   : 18 May 2021
About : It is a simple stone - paper - scissor game
'''

from random import choice
import time
print('''=============================================
                   STONE-PAPER-SCISSOR
=============================================''')
n = int(input("\n\nHow many round do you want to play : "))
word = ["stone", "paper", "scissor"]
c = 0
u = 0

while n>0:
    print("\n say your choice (stone, paper, scissor) ")
    print("\n")
    computer = choice(word)
    user = input("User : ")
    print(f"Computer : {computer}")
    usr = user.lower()
    if usr in word:
       if usr==computer:
          print("Tie")
       elif usr=="stone" and computer=="paper":
           print("Computer wins")
           c = c+1
       elif usr=="paper" and computer=="stone":
            print("User wins")
            u = u + 1
       elif usr=="scissor" and computer=="stone":
            print("Computer wins")
            c = c + 1
       elif usr=="stone" and computer=="scissor":
            print("User wins")
            u = u + 1
       elif usr=="paper" and computer=="scissor":
           print("Computer wins")
           c = c + 1
       elif usr=="scissor" and computer=="paper":
           print("User wins")
           u = u+1
       else:
           print("something wrong")
    else:
       print("oops u entered a invalid key")
    n = n-1
    print("--------------------------------------------------")
time.sleep(1)

print(f'''
================================================
                  SCORE BOARD 
================================================
COMPUTER               | USER                   |
================================================
        {c}            |        {u}                |
================================================''')
if c>u:
    print("COMPUTER WINS")
elif u>c:
    print("USER WINS")
else:
    print("TIE")


