for row in range(1,10):
    for space in range(row,9):
        print(" ",end=" ")
    for star in range(0,row):
        print(" ",row," ",end=" ")
    print("")

for row in range(1,8):
    for col in range(1,8):
        if col<=row:
            print(row,end=" ")
        else:
            print(col,end=" ")
    print()

for row in range(10,-1,-1):
    for col in range(0,row+1):
        print(" ",col," ",end=" ")
    print("\r")

x=""
for i in "python":
    x+=i
    print(x)

for i in range(0,9):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(9, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

for row in range(1,5):
    for space in range(row,5):
        print(" ",end=" ")
    for col in range(1,row+1):
        print(" ",row*col," ",end=" ")
    print()

for row in range(1,9):
    for space in range(row,9):
        print(" ",end=" ")
    for col in range(1,row+1):
        print(col," ",end=" ")
    print("\r")
else:    
    for row in range(9,0,-1):
        for space in range(row,9):
            print(" ",end=" ")
        for col in range(1,row+1):
            print(col," ",end=" ")
        print("\r")

for row in range(1,10):
    for space in range(row,10):
        print(" ",end="")
    for col in range(0,row):
        print("  ",col,"  ",end=" ")
    print()

for row in range(1,10):
    