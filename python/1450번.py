from itertools import combinations
import sys
input=sys.stdin.readline
N,C=map(int,input().split())
li=list(map(int,input().split()))
liA=li[:N//2]
liB=li[N//2:]
A=[]
B=[]
for i in range(len(liA)+1):
    for j in combinations(liA,i):
        A.append(sum(j))

for i in range(len(liB)+1):
    for j in combinations(liB,i):
        B.append(sum(j))

B.sort()
res=0

for ele_A in A:
    if ele_A>C:continue

    st=0
    end=len(B)
    while st<end:
        mid=(st+end)//2
        if ele_A+B[mid]>C:
            end=mid
        else:
            st=mid+1
    res+=end
print(res)
