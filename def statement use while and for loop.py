score=[2,15,24,51,35,12,52,45,12,25,32,45,1,2,5,4,6,45,75,85,65,25]
score

def sum(score):
    for i in score:
        if i<25:
            print("failed score is",i)
    
marks=[12,14,25,15,24,51,25,45,222,111,333,11,444,555,444,666,777,999,111,5555,4444]
sum(marks)

def sum2(marks):
    for i in marks:
        if i>25:
            print("passed mark is",i)

sum2(score)

score=[2,15,24,51,35,12,52,45,12,25,32,45,1,2,5,4,6,45,75,85,65,25]

value=0
while value<21:
    if (score[value])==1:
        break
    print(score[value])
    value=value+1

def sum3(score):
    value=0
    while value<21:
        if (score[value])==1:
            break
        print(score[value])
        value=value+1

value=0
while value<21:
    if (score[value])==1:
        value=value+1
        continue
    print(score[value])
    value=value+1

def sum4(score):
    value=0
    while value<21:
        if (score[value])==1:
            value=value+1
            continue
        print(score[value])
        value=value+1

sum4(score)

def sum5(score):
    value=0
    for i in score:
        value=value+i
        print(value)

sum5(marks)

def sum6():
    value1=0
    for i in range(1,10):
        value1=value1+i
    print(value1)

sum6()


nombers=[23,43,22,33,45,44,32,32,34,23,12,4,6,7,8,8]

def sum7():
    value2=0
    for i in nombers:
        if i%2==0:
            value2=value2+i
    print(value2)
sum7()

index=0
while index<len(nombers):
    print(nombers[index])
    index=index+1


values7=0
index=0
while index<len(nombers):
    if nombers[index]%2==0:
        values7=values7+nombers[index]
    index=index+1
print(values7)

def sum10(nombers):
    values7=0
    index=0
    while index<len(nombers):
        if nombers[index]%2==0:
            values7=values7+nombers[index]
        index=index+1
    print(values7)

sum10(nombers)

marks5=[145,21,54,25,12,12,25,42,12,25,24,26]

sum10(marks5)

