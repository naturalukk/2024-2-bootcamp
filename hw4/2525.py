a, b= map(int, input().split())
c = int(input())
d= b+c



if d>=60:
    e=d//60
    d=d-(60*e)
    a=a+(1*e)
    if d==60:
        d=0
if a>=24:
    a=a-24

print(a, d)

