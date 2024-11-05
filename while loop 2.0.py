row=1
while row<9:
    space=row
    while space<9:
        print(" ",end="")
        space=space+1
    col=1
    while col<row+1:
        print(row," ",end="")
        col=col+1
    print()
    row=row+1
else:
    row=9
    while row>0:
        space=row
        while space<9:
            print(" ",end="")
            space=space+1
        col=1
        while col<row+1:
            print(row," ",end="")
            col=col+1
        print()
        row=row-1

row=1
while row<9:
    space=row
    while space<10:
        print(" ",end="")
        space=space+1
    col=1
    while col<row+1:
        print(row," ",end="")
        col=col+1
    print()
    row=row+1

row=1
while row<9:
    space=row
    while space<10:
        print(" ",end="")
        space=space+1
    col=1
    while col<row+1:
        print(row,end="")
        col=col+1
    print()
    row=row+1
else:
    row=9
    while row>0:
        space=row
        while space<10:
            print(" ",end="")
            space=space+1
        col=1
        while col<row+1:
            print(row,end="")
            col=col+1
        print()
        row=row-1

row=1
while row<9:
    space=10
    while space<row:
        print(" ",end="")
        space=space+1
    col=1
    while col<row+1:
        print(row,end="")
        col=col+1
    print()
    row=row+1
else:
    row=9
    while row>0:
        space=10
        while space<row:
            print(" ",end="")
            space=space+1
        col=1
        while col<row+1:
            print(row,end="")
            col=col+1
        print()
        row=row-1


row=1
while row<9:
    space=10
    while space<row:
        print(" ",end="")
        space=space+1
    col=1
    while col<row+1:
        print(row,end="")
        col=col+1
    print()
    row=row+1

row=1
while row<20:
    space=20
    while space<row:
        print(" ",end="")
        space=space+1
    col=1
    while col<row+1:
        print(row*col,end="")
        col=col+1
    print()
    row=row+1
else:
    row=20
    while row>0:
        space=20
        while space<row:
            print(" ",end="")
            space=space+1
        col=1
        while col<row+1:
            print(row*col,end="")
            col=col+1
        print()
        row=row-1

values=[2,3,4,5,3,2,13,1,3,0,4,40,34,2,3,4,5]

index=0
while values[index]!=0:
    print(values[index])
    index=index+1

nombers1=[22,3,4,2,44,0,33,21,34,22]

index=0
while nombers1[index]!=0:
    print(nombers1[index])
    index=index+1

index=0
while nombers1[index]!=33:
    print(nombers1[index])
    index=index+1

index=0
while nombers1[index]!=2:
    print(nombers1[index])
    index=index+1

points=[3,2,4,2,5,3,4,2,5,3,2,5,6,0,4,5,6,2,4,5]

index=0
while points[index]!=0:
    print(points[index])
    index=index+1
