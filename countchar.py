s = input("Input: ")
c = 'a'
count = 0
for i in range (0,len(s)):
    if c==s[i]:
        count+=1
print("Count :",count)        