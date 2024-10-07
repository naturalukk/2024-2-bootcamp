s,t = input().split()

list_s=[]
list_t=[]
list_s=list(s)
list_t=list(t)

len_s=len(s)
len_t=len(t)
a=0
b=0
c=0

while b < len_t:
    if list_s[a] == list_t[b]:
        a=a+1
        b=b+1
        c=c+1
        if c==len_s:
            break
        if c!=len_s:
            continue
    elif list_s[a] != list_t[b]:
        b=b+1
        continue
    
    
if c == len_s:
    print("Yes")
elif c != len_s:
    print("No")




# print(s)
# print(t)
# print(list_s)
# print(list_t)
# print(len_s)