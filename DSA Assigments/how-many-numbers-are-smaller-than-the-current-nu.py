# how-many-numbers-are-smaller-than-the-current-number
arr=list(map(int,input().split()))
arr1=[]
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]>arr[j]:
            count+=1
    arr1.append(count)
print(arr1)