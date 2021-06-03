'''
Author : Amjad
Date   : 3 JUN 2021 11.30 PM
About  : Hang man game using PYTHON
'''

#IMPORTED PYTHON LIBRARIES
import random
import os
import time
import word_list
#from colorama import Fore

def g_m(i):
    if i==2:
        g_2()
    elif i==3:
        g_3()
    elif i==4:
        g_4()
    else:
        g_p()
    

def g_1():
    print(f'''--------------
|            |            
|            o
|
|
|
|
|
|''')

def g_2():
     print(f'''--------------
|            |            
|            0
|           
|            
|           
|
|
|''')

def g_3():
     print(f'''--------------
|            |            
|            0
|           /|\\
|            
|           
|
|
|''')

def g_4():
     print(f'''--------------
|            |            
|            0
|           /|\\
|            |
|           / \\
|
|
|''')

def g_p():
     print(f'''--------------
|            |            
|            o
|           
|            
|            0
|           /|\\
|            |
|           / \\''')





#A FUNCTION TO PRINT HEADING WITH SHOWING ATTEMPT
def head(i):
    print(f'''------------------------------------------------
    -
                    HANG MAN

--------------- ATTEMPT = {i} of 4-----------------\n\n''')

# a function to check the answer
def answer(word, limit):
    i = 0
    tem = []
    temp = ""
    Guess = input("Guess the word : ")
    guess = Guess.upper()
    for char in guess:
        if char in word:
            tem.insert(i, char)
        else:
            tem.insert(i, "_")
        i = i+1
    
    return temp.join(tem)
    


head(1)
g_1()
words = ["apple", "banana", "pappaya", "car", "bike"]
Word = random.choice(words)
word = Word.upper()
limit = len(word)
print("\n\n", " _ " * limit, "\n\n")
i = 1
result = False

while 5>i:
    if i-1 != 0:
      head(i)
      
    
    temp = answer(word, limit)
    ans = ''
    
    for ch in temp:
      ans = ans + ch + ' '
   

    temp_size = len(temp)
    
    if limit<temp_size:
        print(f"""Breaked limit (only {limit} letters needed""")
        g_m(i)

    elif limit>temp_size:
        print(f"""{limit} letters needed""")
        g_m(i)

    elif limit==temp==word:
        g_p()
        result = True
        print("YOU ARE MY LIFE SAVER")
        print(ans)
    elif limit==temp:
         print(f'''KEEP GOING''')
    
    else:
        print(f'''KEEP GOING       {limit} letters needed''')
        g_m(i)
        

    if result==True:
        break   
   
    time.sleep(5)
    os.system("cls") # in ubundu cls -> clear
    print(f"""HINT : {limit} letters needed""")
    i = i+1

print("NIRTTHI VERAVALLA PANIKKUM PODO")
    

