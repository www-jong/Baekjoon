import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

N=int(input())
M=int(input())

def find(a):
    if a==nodes[a]:
        return a
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


nodes=[i for i in range(N+1)]
for i in range(1,N+1):
    tmp=[0]+list(map(int,input().split()))
    for j in range(i+1,N+1):
        if tmp[j]==1:
            union(i,j)

li=list(map(int,input().split()))
res="YES"
parent=find(li[0])
for i in range(1,M):
    if parent!=find(li[i]):
        res="NO"
        break
print(res)