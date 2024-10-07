a=int(input())
b=1

if a>0 :
    for i in range(1,a+1) :
        b = b * i
elif a==0 :
    b=1

print(b)
