d = int(input("Enter the linenumber to delet line"))
s = ""

with open('another.txt', 'r') as f:
    a = "b"
    i = 0
    while a:
        i += 1
        a = f.readline()
        print(a, end="")
        if i == d:
            continue
        s = s + a
with open('another2.txt', 'w') as fp:
    fp.write(s)

f.close()
fp.close()
  
