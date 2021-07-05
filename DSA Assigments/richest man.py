# richest man
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
maxx=0
for i in range(n):
    sumx=sum(arr[i])
    if maxx<sumx:
        maxx=sumx
print(maxx)