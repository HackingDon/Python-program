a = [-2,-3,4,-1,-2,1,5,-3]
length = len(a)            
maximum = 0
for i in range (0,length):
    sum = a[i]
    for j in range (i+1,length):
        sum += a[j]
        if sum>maximum:
            maximum = sum   
print("maximum sum of subarray", maximum)               
