import sys
input=sys.stdin.readline

N,P=map(int,input().split())
contury=[0]
li=[0]
for i in range(N):
    contury.append(int(input()))
for i in range(P):
    S,E,L=map(int,input().split())
    li.append([S,E,L+li[E]])
    li.append([E,S,L+li[S]])
    
nodes=[0]*(N+1)

def find(a):
    if a==nodes[a]:
        return a
    return find(nodes[a])

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b
