#intersection of one array
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n,m=len(arr1),len(arr2)
arr3=[]
if n>m:
    for i in range(m):
        if arr2[i] in arr3:
            continue
        else:
            if arr2[i] in arr1:
                arr3.append(arr2[i])
else:
    for i in range(n):
        if arr1[i] in arr3:
            continue
        else:
            if arr1[i] in arr2:
                arr3.append(arr1[i])
print(arr3)