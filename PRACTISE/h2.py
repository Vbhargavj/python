def is_leap(year):
    leap = False
    if year%4 == 0 :
        leap = True
        if year%100 == 0:
            leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
print(1990%4)
