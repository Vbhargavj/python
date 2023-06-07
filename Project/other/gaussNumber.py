# this module give random number
import random
# this is count how many try complete
guess = 1
rnum = random.randint(1, 100)
print(rnum)

# this is taken output from user
unum = int(input("Enter your choise"))

while rnum!=unum :
    if rnum < unum:
        unum = int(input("Enter smaller number"))
    elif rnum > unum:
         unum = int(input("Enter larger number"))

    guess+=1      
with open('D:\\coding\\code program\\python program\\Project\\high.txt','r') as f:
    a =f.read()
    ra = int(a)
if ra>guess:
    with open('D:\\coding\\code program\\python program\\Project\\high.txt','w') as f:
        f.write(str(guess)) 

print("\n****You enter right choise****\n")
print(f"You guess the number in {guess}")    