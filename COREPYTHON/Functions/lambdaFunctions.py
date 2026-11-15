def f1(n):
    n*n

f1(10)

n = lambda n:n*n
n(2)

s = lambda a,b:a+b
s(1,3)

s = lambda a,b: a if a > b else b

def isEven(x):
    if x%2 == 0:
        return x

l=[3,10,20,30,40]
l2=list(filter(isEven, l))
print(l2)

l3=list(filter(lambda x : x%4==0, l))
print(l3)

def double(x):
    x = x*2
    return x

d = double(10)
print(d)

l=[10,20,30,40]
m=list(map(lambda x : x*2, l))
print(m)

import functools as f
r = f.reduce(lambda x,y:x+y,l)
print(r)



