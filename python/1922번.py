import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
M=int(input())

li=[]
nodes=[i for i in range(N+1)]
def find(a):
    if a==nodes[a]:
        return a
    else:
        nodes[a]=find(nodes[a])
        return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

for _ in range(M):
    A,B,C=map(int,input().split())
    li.append([A,B,C])
li.sort(key=lambda x:x[2])

res=0
for x,y,val in li:
    if find(x)!=find(y):
        res+=val
        union(x,y)

print(res)