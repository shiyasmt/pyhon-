a='gOoDmOrnInGtUeSdAy'
for value in a:
    if value.isupper():
        print(value)
for value in a:
    if value.islower():
        print(value)

list1=[]
for value in a:
    if value.islower():
        list1.append(value)
list1
list2=[]
for value in a:
    if value.isupper():
        list2.append(value)
list2
list3=[]
list4=[]
for value in a:
    if value.islower():
        list3.append(value)
    else:
        list4.append(value)
list4
list3
marks=[10,20,30,40,50,60]
sum1=0
for value in marks:
    sum1=sum1+value
sum1
count=0
for value in a:
    if value.islower():
        count=count+1
count
count2=0
for value in a:
    if value.isupper():
        count=count+1
count2
b='HeYtuEsdaY'
list5=[]
list6=[]
for value in b:
    if value.islower():
        list5.append(value)
    else:
        list6.append(value)
list5
list6
count5=0
for value in b:
    if value.islower():
        count5=count5+1
count5
count6=0
for value in b:
    if value.isupper():
        count6=count6+1
count6
count7=0
count8=0
upperlist=[]
lowerlist=[]
for value in b:
    if value.isupper():
        count7=count7+1
        upperlist.append(value)
    else:
        count8=count8+1
        lowerlist.append(value)
count7
count8
upperlist
lowerlist
sum5=0
for value in range(1,51):
    sum5=sum5+value
sum5
sum6=0
for value in range(1,51,2):
    sum6=sum6+value
sum6
for value in range(1,51):
    if value%2==0:
        print(value)
sum10=0
for value in range(1,51):
    if value%2==0:
        sum10=sum10+value
sum10
sum11=0
for value in range(1,51):
    if value%2==1:
        sum11=sum11+value
sum11
sum12=0
sum13=0
for value in range(1,51):
    if value%2==0:
        sum12=sum12+value
    else:
        sum13=sum13+value
sum12
sum13
"*"*6

for value in range(1,7):
    print(value*"*")

for value in range(1,15):
    print(value*"*")

for value in range(1,3):
    print(value*"*")

for value in range(7,0,-1):
    print(value*"*")

for value in range(99,88,-1):
    print(value*"*")

for value in range(33,89):
    print(value*"*")

for value in range(66,33,-1):
    print(value*"*")

for value in range(99,0,-1):
    print(value*"*")

for value in range(11,0,-1):
    print(value*"shiyas")

for value in range(33,0,-1):
    print(value*"#")

for value in range(99,0,-1):
    print(value*"@")

for value in range(6,0,-1):
    print(value*"*")

for value in range(1,7):
    print(" "*(7-value),value*"  *  ")

