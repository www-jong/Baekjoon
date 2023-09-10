N,M=map(int,input().split())
A=sorted(list(map(int,input().split())),reverse=True)
B=sorted(list(map(int,input().split())))
r=0
idx=0
for i in B:
    if A[idx]>i:
        r+=A[idx]-i
        idx+=1
    if idx==N:break
print(r)
