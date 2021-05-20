'''
Author : Amjad
Date   : 18 May 2021
About : It is a simple stone - paper - scissor game
'''

from random import choice
import time

computer_option = ["stone", "paper", "scissor"]
user_option = ["stone", "paper", "scissor", "quite"]

c = 0
u = 0
count = 0
t = 0

while True:
    print('''=============================================
                   STONE-PAPER-SCISSOR
    =============================================''')
 
    print("\n say your choice (stone, paper, scissor, quite (to quite this game)) ")
    print("\n")
    computer = choice(computer_option)
    user = input("User : ")
    print(f"Computer : {computer}")
    usr = user.lower()
    if usr in user_option:
       if usr==computer:
          print("Tie")
          t =+ 1
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
       print("oops u entered a invalid key \nTry again")
       t =+ 1
    print("--------------------------------------------------")
    if usr=="quite":
       break
    count =+ 1
    time.sleep(1)
print(f'''
================================================
                  SCORE BOARD 
================================================
COMPUTER               | USER                   |
================================================
        {c}            |        {u}             |
================================================
No.of round u played   |        {count}         |
================================================
No.of round tied       |         {t}            |
================================================''')
if c>u:
    print("COMPUTER WINS")
elif u>c:
    print("USER WINS")
else:
    print("TIE")
