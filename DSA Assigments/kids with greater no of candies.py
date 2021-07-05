# kids with greater no of candies
candies=list(map(int,input().split()))
extra=int(input())
maxx=max(candies)
n=len(candies)
output=[False]*n
for i in range(n):
    if candies[i]+extra>=maxx:
        output[i]=True
print(output)
    