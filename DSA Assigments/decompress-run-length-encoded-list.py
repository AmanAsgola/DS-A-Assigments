# decompress-run-length-encoded-list
arr=list(map(int,input().split()))
i = 0
ans = []
while i < len(arr):
    ans += [arr[i+1]]*arr[i]
    i += 2
print(ans)