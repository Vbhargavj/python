marks = {"BHARGAV": 100, "JEET": 70, "BHUMIK": 99, "JAY": 10}

grade = {}
for key in marks:

    val = marks[key] 

    if val in range(91, 101):
        grade[key] = "Outstanding"
    elif val in range(81, 91):
        grade[key] = "exceeded exception"
    elif val in range(70, 81):
        grade[key] = "Acceptable"
    else:
        grade[key] = "Failed"

for key in grade:
    print(f"Student name :{key}  Grade : {grade[key]}")

print(grade)
