
ans = "yes"

User = ""
Bid = 0

while ans.lower() != "no":

    user = input("Enter the bider name : ")
    bid = int(input("Enter the biding values : "))

    if bid > Bid:
        User = user
        Bid = bid

    ans = input("if any person for bid than write yes otherwise write no : ")
    print(ans)

print(f"The person {User} is bid {Bid} values on item")