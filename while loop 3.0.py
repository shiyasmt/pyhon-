marks=[1,2,5,4,1,2,5,4,2,5,4,1,0,2,5,4,5,6,2,1,4]
index=0
while marks[index]!=0:
    print(marks[index])
    index=index+1

index=0
while marks[index]!=6:
    print(marks[index])
    index=index+1

index=0
while marks[index]!=4:
    print(marks[index])
    index=index+1

marks.count(4)
marks=[1,2,5,4,1,2,5,4,2,5,4,1,0,2,5,4,5,6,2,1,4]
count=0
index=0
while count!=2:
    if marks[index]==4:
        count=count+1
        print(marks[index])
        index=index+1
        if count==2:
            break
    print(marks[index])
    index=index+1

count=0
index=0
while count!=4:
    if marks[index]==2:
        count=count+1
        print(marks[index])
        index=index+1
        if count==4:
            break
    print(marks[index])
    index=index+1

marks.count(2)

count=0
index=0
while count!=2:
    if marks[index]==1:
        count=count+1
        print(marks[index])
        index=index+1
        if count==2:
            break
    print(marks[index])
    index=index+1

count=0
index=0
while count!=2:
    if marks[index]==5:
        count=count+1
        print(marks[index])
        index=index+1
        if count==2:
            break
    print(marks[index])
    index=index+1

a=input("enter a value and 0 for quit")
while a!="0":
    print(a)
    a=input("enter a value and 0 for quit")

a=input("enter a value and 5 for quit")
while a!="5":
    marks.append(a)
    a=input("enter a value and 5 for quit")
    
marks