string = input("Enter string ")
stack = []
new = []
for i in range (0,len(string)):
    stack.append(string[i])
for i in range (0,len(stack)):
    new.append(stack.pop())
print(''.join(new))    
