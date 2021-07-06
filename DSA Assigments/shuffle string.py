# shuffle string
s = input()
indices = list(map(int,input().split()))
res=[None]*len(indices)
for i in range(len(s)):
    res[indices[i]]=s[i]
print("".join(res))