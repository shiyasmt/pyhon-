score=[1,2,4,6,4,1,2,3,5,4,7,8,5,4,1,2,5,4]
def sum(score):
    sum=0
    for i in score:
        sum=sum+i
    return sum
a=sum(score)
a

values=[1,3,2,34,32,44,55,44,32,12,23,35,66,88,46,48]

def evenvalues(values):
    list1=[]
    for i in values:
        if i%2==0:
            list1.append(i)
    return list1

c=evenvalues(values)
c

def pattern(a):
    for row in range(1,a):
        for space in range(row,a):
            print(" ",end=" ")
        for col in range(1,row+1):
            print(col," ",end=" ")
        print("\r")
    else:    
        for row in range(a,0,-1):
            for space in range(row,a):
                print(" ",end=" ")
            for col in range(1,row+1):
                print(col," ",end=" ")
            print("\r")

pattern(4)
pattern(6)

def breakzero():
    a=input()
    while a!="0":
        print(a)
        a=input()

breakzero()

def appendtolist():
    list1=[]
    a=input("enter a value and 0 for quit")
    while a<"5":
        list1.append(a)
        a=input("enter a value and 0 for quit")
    print(list1)

appendtolist()



def appendtolist():
    list2=[]
    a=input("enter a value and 0 for quit")
    while a>"5":
        list2.append(a)
        a=input("enter a value and 0 for quit")
    print(list2)
appendtolist()

def max(x,y):
    if x>y:
        return x
    else:
        return y

max(25,5)
max(2515125,2455142)

def max2(x,y,z):
    if x>y and x>z:
        return x
    elif y>z and x<y:
        return y
    else:
        return z

max2(10,25,15)
max2(1254,25165,1245125)
max2(1234,34,54)
max2(40,35,79)


def min(x,y,z):
    if x<y and x<z:
        return x
    elif y<z and x>y:
        return y
    else:
        return z

min(13,24,25)
min(112233,123,11122)

