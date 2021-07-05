# shuffel the array
arr=list(map(int,input().split()))
n=int(input())
res=[]
for i in range(n):
    res.append(arr[i])
    res.append(arr[i+n])
print(res)