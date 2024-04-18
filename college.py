
a= input("Enter the number\n")


for i in range(len(a)):
    if(a[i]>='a' and a[i]<='z'):
        print(ord(a[i])-96,end=", ")
    if(a[i]>='A' and a[i]<='Z'):
        print(ord(a[i])-64+26,end=", ")