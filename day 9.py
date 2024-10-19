a=[1,2,3,4,5,6,7,8]
for value in range(0,9):
    print(a[value])
for value in range(len(a)-1,-1,-1):
    print(a[value])
b=['shiyas','salif','fazil','riswan','favas','ansil','shahil']
for name in range(0,len(b)):
    print(b[name])
for name in range(0,2):
    print(b[name])
for name in range(0,3):
    print(b[name])
for name in range(0,len(b)):
    print(b[name])
for name in b:
    print(name[:3])
for name in b:
    print(name[::2])
for name in b:
    print(name[0:1])
for name in b:
    print(name[2:4])
c="HeLloGoOdMoRnIngsAtUrdAy10,26,10,{[()]}"
for name in c:
    print(name[0])
dir(c)
for value in c:
    if value.isupper():
        print(value)
for value in c:
    if value.islower():
        print(value)
list1=[]
for value in c:
    if value.islower():
        list1.append(value)
list2=[]
for value in c:
    if value.isupper:
        list2.append(value)
list3=[]
list4=[]
for value in c:
    if value.isupper():
        list3.append(value)
    else:
        list4.append(value)
print(list3)
print(list4)
list3=[]
list4=[]
others=[]
for value in c:
    if value.isupper():
        list3.append(value)
    elif value.islower():
        list4.append(value)
    else:
        others.append(value)
list3
list4
others
nombers=[10,15,20,25,18,12]
type(nombers)
sum(nombers)
for value in nombers:
    print(sum(nombers))


h=[10,25,15,25,23,54,58,65,25,55]

sum1=0
for value in h:
    sum1=sum1+value
sum1
sum1=0
for value in h:
    sum1=sum1-value
sum1
sum2=0
for value in h:
    sum2=sum2*value
sum1
i=[1,2,3,4,5,6,7]
sum4=0
for value in i:
    sum4=sum4/value
sum4