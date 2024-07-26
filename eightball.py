a = [3,3,3,3,3,2,3,3]
def defective(arr):
    c1 = arr[0:3]
    c2 = arr[3:6]
    c3 = arr[6:]
    if add(c1) == add(c2):
        if c3[0]>c3[1]:
            return c3[1]
        else:
            return c3[0]
    elif add(c1) > add(c2):
        if c2[0] == c2[1]:
            return c2[2]
        elif c2[0] > c2[1]:
            return c2[1]
        else:
            return c2[0] 
    else:
        if c1[0] == c1[1]:
            return c1[2]
        elif c1[0] > c1[1]:
            return c1[1]
        else:
            return c1[0]  

def add(a):
    sum =0
    for i in range (0,len(a)):
        sum+=a[i]
    return sum
def findval(a,arr):
    for i in range (0,len(arr)):
        if a==arr[i]:
            return i

problem = defective(a)
index = findval(problem,a)

print("The defective value is",problem,"is a ",index,"th ball")

       