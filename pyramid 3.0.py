for row in range(1,10):
    for col in range(0,row):
        print("*",end=" ")
    print(" ")
 for row in range(1,10):
    for space in range(row,9):
        print(" ",end=" ")
    for star in range(0,row):
        print(" * ",end=" ")
    print("")

for row in range(1,9):
    for space in range(row,8):
        print("  ",end="")
    for star in range(0,row):
        print(" ",row," ",end="")
    print("")

for row in range(8,0,-1):
    for space in range(row,8):
        print("  ",end="")
    for star in range(0,row):
        print(" ",row," ",end="")
    print("")

for row in range(0,6):
    for col in range(0,row):
        print("*",end="")
    print("\r")
for row in range(6,0,-1):
    for col in range(0,row):
        print("*",end="")
    print("\r")

for row in range(1,8):
    for col in range(1,8):
        if col <= row:
            print(row,end="")
        else:
            print(col,end="")
    print()

for row in range(1,9):
    for space in range(row,8):
        print("  ",end="")
    for star in range(0,row):
        print("  9 ",end="")
    print("")

