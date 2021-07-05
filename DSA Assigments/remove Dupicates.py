# remove Dupicates from sorted array
arr=list(map(int,input().split()))
res=[]
for i in arr:
    if i in res:
        continue
    else:
        res.append(i)
print(len(res))