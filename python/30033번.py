N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
r=0
for i in range(N):
    if A[i]<=B[i]:
        r+=1
print(r)