input_data=[]
i=0
j=0
a=0
maxx=0

while i<9:
    a=int(input())
    input_data.append(a)
    i=i+1

b=max(input_data)


while j<9:
    if input_data[j]==b:
        maxx=j+1
        break
    else:
        j=j+1



print(max(input_data))
print(maxx)
