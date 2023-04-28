import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(a):
    if a==nodes[a]:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        nodes[b]=a
        counts[a]+=counts[b]

for i in range(int(input())):
    F=int(input())
    nodes={}
    counts={}
    for i in range(F):
        a,b=map(str,input().split())
        if a not in nodes:
            nodes[a]=a
            counts[a]=1
        if b not in nodes:
            nodes[b]=b
            counts[b]=1
        union(a,b)
        print(counts[find(a)])