for row in range(1,10):
    for space in range(row,10):
        print(" ",end="")
    for col in range(1,row+1):
        print(col,end="")
    print("\r")
else:
    for row in range(9,0,-1):
        for space in range(row,10):
            print(" ",end="")
        for col in range(1,row+1):
            print(col,end="")
        print("\r")

list1=[1,2,3,4,5,6]
for value in range(0,6):
    print(list1[value])
value=0
while value<6:
    print(list1[value])
    value=value+1

marks=[10,25,12,20,30,1,50,40,60]

value=0
while value<9:
    print(marks[value])
    value=value+1

grade=["a","b","c","d","e"]

value=0
while value<5:
    print(grade[value])
    value=value+1

value=8
while value>=0:
    print(marks[value])
    value=value-1

for row in range(1,10):
    for col in range(1,10):
        print(row,end="")
    print()           

row=1
while row<10:
    col=1
    while col<10:
      print(row,end="") 
      col=col+1 
    print()
    row=row+1


for row in range(1,7):
    for col in range(1,row):
        print(col,end=" ")
    print("")

row=1
while row<7:
    col=1
    while col<row:
        print(col,end="")
        col=col+1
    print()
    row=row+1

row=1
while row<7:
    space=row
    while space<7:
        print(" ",end="")
        space=space+1
        col=1
    while col<row:
        print(col," ",end="")
        col=col+1
    print()
    row=row+1

row=1
while row<7:
    space=row
    while space<7:
        print(" ",end="")
        space=space+1
        col=1
    while col<row+1:
        print(row," ",end="")
        col=col+1
    print()
    row=row+1
else:
    row=7
    while row>=1:
        space=row
        while space<7:
            print(" ",end="")
            space=space+1
        col=1
        while col<row+1:
            print(row," ",end="")
            col=col+1
        print()
        row=row-1

