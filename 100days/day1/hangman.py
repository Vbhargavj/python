import random
import os
word_list = ["bhargav", "jeet", "nehal"]

rw = random.choice(word_list)
display=[]
display = ["_" for _ in range(len(rw))]
logo='''
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| | ____   ____  | || |   ______     | || |     _____    | |
| ||_  _| |_  _| | || |  |_   _ \    | || |    |_   _|   | |
| |  \ \   / /   | || |    | |_) |   | || |      | |     | |
| |   \ \ / /    | || |    |  __'.   | || |   _  | |     | |
| |    \ ' /     | || |   _| |__) |  | || |  | |_' |     | |
| |     \_/      | || |  |_______/   | || |  `.___.'     | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 


'''
fasi = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    

f = 1
t=0
# print(logo)
while f:
    print(logo)
    print(f"{' '.join(display)}")
    if t>6:
        print("You loose")
        exit(1)
    ic = input("Guess the character : ").lower()
    os.system('cls')
    i=0
    if ic not in rw:
        print("You lose life because the character is not in word")
        print(fasi[t])
        t+=1
    for letter in rw:

        if letter ==ic:
            display[i]=ic            
        i+=1
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("Player won the match")
        f=0