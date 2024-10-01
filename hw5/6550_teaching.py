input_data = []

while True:
    try:
        input_string = input()

        if input_string == "":
            break
        input_data.append(input_string)
    except EOFError:
        break

for line in input_data:
    s, t = line.split()
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