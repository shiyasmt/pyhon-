
b=[]
a=int(input("enter a value"))
sum=0
while a!="0":
    sum=sum+a
    b.append(sum)
    print(b)
    a=int(input("enter a value"))

b

score=[2,1,4,6,3,4,5,4,6,2,1,4,5,8,7,5,4,6,8,7,4,2,4,6,3,1,8]

for i in score:
    if i<5:
        print("failed mark is",i)

for i in score:
    if i>5:
        print("pass mark is",i)

mark=25

if mark<30:
    print("failed mark",mark)

score=[2,1,4,6,3,4,5,4,6,2,1,4,5,8,7,5,4,6,8,7,4,2,4,6,3,1,8]

for i in score:
    while i<5:
        print(i)
        break

value=0
while value<27:
    if (score[value])==8:
        break
    print(score[value])
    value=value+1

value=0
while value<27:
    if (score[value])==8:
        value=value+1
        continue
    print(score[value])
    value=value+1

def sum1(score):
    value=0
    while value<27:
        if (score[value])==8:
            value=value+1
            continue
        print(score[value])
        value=value+1

sum1(score)
def sum2(score):
    value=0
    while value<27:
        if (score[value])==8:
            break
        print(score[value])
        value=value+1

sum2(score)

marks=[10,21,12,52,54,12,54,12,45,12,54,52,12,14,25,12,45]

def sum3(marks):
    for i in marks:
        if i<25:
            print(i)

sum3(marks)

values=[2,25,24,56,25,35,12,35,62,54,12,32,12,52,45,26,15,25,35,15,25,14,26,15,17,18,25]

sum3(values)

sum2(values)

sum1(values)

a=[1,2,1,0,15,24,10,25,10,21,20,30,10,50,20]
