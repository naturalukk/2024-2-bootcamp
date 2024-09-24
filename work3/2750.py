a=set()
b=input()
sb=int(b)

for i in range(sb):
    c = input()
    e=int(c)
    a.add(e)


d=sorted(a)

for i in range(sb):
    print(d[i])
