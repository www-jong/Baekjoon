L=int(input())
S=sorted([0]+list(map(int,input().split())))
n=int(input())
r=0

c=0
for i in range(L+1):
    if S[i]>n:
        c=i-1
        break
print(c,S)
for i in range(S[c]+1,n+1):
    for j in range(n,S[c+1]):
        if i!=j:
            print(i,j)
            r+=1
print(r)