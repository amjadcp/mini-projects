import random
import os
import time

def head(i):
    print(f'''---------------------------------
                        HANG MAN
--------------- ATTEMPT = {i} of 4-----------------\n\n''')

def main(word, limit):
    i = 0
    tem = []
    temp = ""
    guess = input("\nGuess the word : ")
    for char in guess:
        if char in word:
            tem.insert(i, char)
        else:
            tem.insert(i, "_")
        i = i+1
    
    return temp.join(tem)
'''
def update(temp, limit):
    i = 0
    str = []
    store = ""
    for char in temp:
        if char in '''
    
    


head(0)
words = ["banana"]
word = random.choice(words)
limit = len(word)
print(" _ " * limit)
i = 1
result = ""
while 5>i:
    if i-1 != 0:
      head(i)
    temp = main(word, limit)
    ans = ''
    for ch in temp:
      ans = ans + ch + ' '
    print("\n", ans[:-1], "\n")

    temp_size = len(temp)
    if limit<temp_size:
        print(f"""Breaked limit (only {limit} letters needed""")
    elif limit>temp_size:
        print(f"""{limit} letters needed""")
    else:
        result = "YOU WINS"
        print(result)
        print(word)
    i = i+1
    if result != "":
        break
    time.sleep(1)
    os.system("cls") # in ubundu cls -> clear
    

