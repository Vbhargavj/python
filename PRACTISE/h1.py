if __name__ == '__main__':
    n = int(input().strip())
if n%2 != 0 :
    print("Weird")

elif n%2 == 0 :
    if  2>n and 5>n :
        print("Not Weird") 
    elif 6<n and 20>n :
        print("Weird")
    elif n>20 :
        print("Not Weird")