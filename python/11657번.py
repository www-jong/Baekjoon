import sys
n,m=map(int,input().split())
INF=int(1e9)
graph=[]
distance=[INF]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))
    
def func(s):
    distance[s]=0
    for i in range(n): # 모든점의갯수-1 만큼 반복
        for q,w,e in graph: # 모든경로 확인
            if distance[q] != INF and distance[w]>e+distance[q]:
                distance[w]=e+distance[q]
                if i==n-1:# 마지막 사이클에서도 작동하면->음의사이클
                    return True
    return False
check=func(1)
if check==True:
    print("-1")
else:
    for i in range(2,n+1):
        if distance[i]==INF:
            print("-1")
        else:
            print(distance[i])