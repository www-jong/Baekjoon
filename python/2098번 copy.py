import sys
input=sys.stdin.readline
N=int(input())
nodes=[i for i in range(N+1)]
li=[]
def find(a):
    if nodes[a]==a:
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

for i in range(1,N+1):
    tmp=list(map(int,input().split()))
    for j in range(1,N+1):
        li.append([i,j,tmp[j-1]])

li.sort(key=lambda x:x[2])

