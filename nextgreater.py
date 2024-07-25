stack = [4,26,5,7,22]


for i in range (0,len(stack)):
    new = []
    for j in range (i+1,len(stack)):
        if stack[i]<stack[j]:
            new.append(stack[j])
    if bool(new):
        print(stack[i],"-->",min(new))
    else:
        print(stack[i],"-->",-1)            