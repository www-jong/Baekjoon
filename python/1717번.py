import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())

nodes=[i for i in range(n+1)]

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

for i in range(m):
    c,a,b=map(int,input().split())
    if c==0:
        if a!=b:
            union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')