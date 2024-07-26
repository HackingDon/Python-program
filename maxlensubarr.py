a = [-2,-3,4,-1,-2,1,5,-3]

k=7
max_len = 0
length = len(a)
s=0
e=0
for i in range (0,length):
    sum = a[i]
    new = []
    for j in range (i+1,length):
        sum += a[j]
        new.append(a[j])
        if sum==k:
            if max_len<len(new):
                max_len = len(new)
                s=i
                e=j
print("maximum length of subarray", max_len)
print(a[s:e+1])                
