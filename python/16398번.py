import sys
input=sys.stdin.readline
N=int(input())
def find(a):
    if a==nodes[a]:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]

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
li=[]
for i in range(1,N+1):
    tmp=[0]+list(map(int,input().split()))
    for j in range(i+1,N+1):
        li.append([i,j,tmp[j]])
li.sort(key=lambda x:x[2])
res=0
for i in range(len(li)):
    a,b,v=li[i]
    if find(a)!=find(b):
        res+=v
        union(a,b)
print(res)