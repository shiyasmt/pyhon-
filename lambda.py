def summ(n):
    n=n+1
    return n
summ(5)

summ=lambda n,s: n+s
print(summ(5,6))

multiply=lambda n,m: n*m
print(multiply(6,3))

divide=lambda n,m: n/m
print(divide(6,3))

sum2=lambda n,m,s,t: n+m+s+t
print(sum2(2,4,6,8))

a=lambda m,n,o,p,q: m+n/o+p+q
print(a(10,20,4,6,5))

b=lambda m,n,o,p,q,r:m+n+o+p*q*r
print(b(4,5,6,7,8,9))


def ev(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
ev(5)

"even" if 4%2==0 else "odd"

ev=lambda n: "even" if n%2==0 else "odd"
print(ev(6))


for i in range(6):
    print(i**2)

[i**2 for i in range(6)]
sr=lambda n: [i**2 for i in range(n)]

print(sr(2))

ps=lambda n: "true" if n>5 else "false"
print(ps(4))

hs=lambda n: [i/5 for i in range(n)]
print(hs(6))

a=lambda n: n.lower()
print(a("shiYAs"))
b=lambda n: n.upper()
print(b("shiYAs"))

c=lambda n:sorted(n)
print(c([3,2,4,6,5,4,3,6,4]))

d=lambda n:sorted(n)
print(d([44,3,2,5,66,77,55,44,33,22,2,4,1,0,9,88,77]))

e=lambda n:sorted(n)
print(e([(10,20),(12,13),(9,3)]))

x=[(2,9,3,5,1,8,4,9,3),(1,2,3,5,7,4,5,3),(0,1,22,3,4,5,3,3)]
x.sort(key=lambda x:x[2])
print(x)