# Count the Number of Consistent Strings
allowed = input()
words = list(map(int,input().split()))
count=0
for i in words:
    for j in i:
        if j in allowed:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        count+=1
print(count)