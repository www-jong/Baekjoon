import sys
input=sys.stdin.readline

N,M=map(int,input().split())
gods=[[] for i in range(N+1)]
li=[]
now=0
nodes=[i for i in range(N+1)]

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

for i in range(1,N+1):
    a,b=map(int,input().split())
    gods[i]=[a,b]

for i in range(1,M+1):
    a,b=map(int,input().split())
    union(a,b)

for i in range(1,N+1):
    for j in range(i+1,N+1):
        x1,y1=gods[i]
        x2,y2=gods[j]
        lens=(abs(x2-x1)**2+abs(y2-y1)**2)**0.5
#        print(f'makes {i}:{j} -> {lens}')
        li.append([i,j,lens])

li.sort(key=lambda x:x[2])
weight=0
i=0
for i in range(len(li)):
    a,b,v=li[i]
    if find(a)!=find(b):
        weight+=v
        union(a,b)
#        print(f'combine {a}:{b}')
print('%.2f'%(weight))