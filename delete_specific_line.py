# this function is use to specific re write line  
def dele():
    # the line numbre was given by user  
    d = int(input("Enter the linenumber to delet line"))
    s = ""  #this is store all text data from file so intilise
    # read all data from main file  
    with open('simple1.txt', 'r') as f:
        a = "b"
        i = 0
        while a:
            i += 1

            a = f.readline() #read line by line 
            print(a, end="") #this readline functoin is make automatically new line so use 
             # when line is equal to the given line below condition is true     
            if i == d:
                # this is take text from user and jont it
                k = input("enter text to write in line")
                a =  k + "\n" #this is use because output is mixed  
                # store all data from file in  s
            s = s + a
    # this is create temp file and store edit data   
    with open('another2.txt', 'w') as fp:
        fp.write(s)

    f.close()
    fp.close()
    
dele()

# this is use rename file 
import os

# this is search name in open file and return set
s = os.listdir() 

#this is take name of file 
name = input("Enter the name of file to rename") 

if name in s :
    n = 1
else :
    n = 0 

# this is use to check valid file  name enter by user 
if n == 0  :
    print("please Enter valid name of  file")
    quit()
        
#this is use to give new name of file  
rname = input("Enter the new name")

f = open(name,"r")
r = f.read()

f = open(rname,"w")
f.write(r)

# after copy of file remove main file in file
os.remove(name)  