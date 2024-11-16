#if
mark=70
if mark>60:
    print("passed mark is",mark)

mark1=[20,32,60,88,97]
for i in mark1:
    if i>60:
        print("passed mark is",i)

mark1

for i in mark1:
    print(i)

markstotal=[]

a=int(input("enter a integer value and appent to marktotal"))
sum=0
while a>10:
    sum=sum+a
    print(sum)
    markstotal.append(a)
    a=int(input("enter a integer value and appent to marktotal"))

markstotal

mark=[]

a=input("enter a value and 0 for quit")
while a!="0":
    print(a)
    a=input("enter a value and 0 for quit")

mark2=[]

a=int(input("enter a integer value <10 and print"))
while a<10:
    print(a)
    mark2.append(a)
    a=int(input("enter a integer value <10 and print"))


a=int(input("enter a value"))
while a>100:
    print(a)
    a=int(input("enter a value"))

values=[10,25,10,23,12,15,24,12,13,16,4,21,12,35,13,6,9,8,6,5,6,24,25,24,23]

for i in values:
    if i<15:
        print("failed mark is",i)


points=[3,6,5,2,1,4,5,2,3,6,1,5,8]
for i in points:
    if i>5:
        print("passed points",i)
