a, b, c= map(int, input().split())

if ((a==b)&(a==c)):
    d=a*1000+10000 
elif ((a==b)or(a==c)or(b==c)):
    if ((a==b)or(a==c)):
        d=a*100+1000
    elif (b==c):
        d=b*100+1000
else:
    if ((a>b)&(a>c)):
        d=a*100
    elif ((b>a)&(b>c)):
        d=b*100
    elif ((c>a)&(c>b)):
        d=c*100

print(d)