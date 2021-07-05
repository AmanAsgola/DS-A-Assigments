#Remove Elements
arr=list(map(int,input().split()))
val=int(input())
count=0
for i in arr:
    if i==val:
        continue
    else:
        count+=1
print(count)