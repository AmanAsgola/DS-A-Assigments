# Create Target Array in the Given Order
arr=list(map(int,input().split()))
index=list(map(int,input().split()))
array=[]
for i in range(len(arr)):
    array.insert(index[i],arr[i])
print(array)