a=set()
b=int(input())

for i in range(b):
    c = int(input())
    a.add(c)

d=sorted(a)

for i in range(b):
    print(d[i])
