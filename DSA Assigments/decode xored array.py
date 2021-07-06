# decode xored array
arr=list(map(int,input().split()))
first=int(input())
arr1=[]
arr1.append(first)
for i in range(len(arr)):
    arr1.append(arr1[i]^arr[i])
print(arr1)