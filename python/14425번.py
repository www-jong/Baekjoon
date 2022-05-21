n,m=map(int,input().split())
N=set()
s=0
for i in range(n):
    N.add(input())
for i in range(m):
    if input() in N:
        s+=1
print(s)