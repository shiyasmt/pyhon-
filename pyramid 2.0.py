marks=[10,20,15,30,35,65,45,85,50]
type(marks)
for value in range(1,7):
    print(value*"*")
for value in range(1,7):
    print(" "*(7-value),(value*" * "))

for value in marks:
    print(value)

marks2=[1,2,3,4,5,6,7,8,9,10]
for value in marks2:
    print(" "*(11-value),(value*" "))

for row in range(1,6):
    for col in range(0,5):
        print("*",end=" ")
    print("")

for row in range(1,8):
    for col in range(0,5):
        print("*",end=(" "))
    print("")

for row in range(1,12):
    for col in range(0,10):
        print("*",end=(" "))
    print("")

for row in range(1,12):
    for col in range(0,row):
        print("*",end=(" "))
    print("")

for row in range(1,12):
    for col in range(0,row):
        print("*",end=" ")
    print("")

for row in range(12,-1,-1):
    for col in range(row,-1,-1):
        print(row,end=" ")
    print("")

for row in range(1,6):
    for col in range(0,row):
        print("5",end=" ")
    print("")

for row in range(1,7):
    for col in range(1,row):
        print(col,end=" ")
    print("")

for row in range(1,6):
    for space in range(row,5):
        print(" ",end=" ")
    for star in range(0,row):
        print(" * ",end=" ")
    print("")
