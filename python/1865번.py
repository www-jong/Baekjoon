TC=int(input())
INF=int(1e9)


def func(s):
    distance=[INF]*(n+1)
    distance[s]=0
    for i in range(n): # 모든점의갯수-1 만큼 반복
        for q,w,e in graph: # 모든경로 확인
            if distance[q] != INF and distance[w]>e+distance[q]:
                distance[w]=e+distance[q]
                if i==n-1:# 마지막 사이클에서도 작동하면->음의사이클
                    return True
    return False



for _ in range(TC):
    n,m,w=map(int,input().split())#지점수,도로수,웜홀수
    graph=[]
    ch=0
    for i in range(m):
        a,b,c=map(int,input().split())
        graph.append((a,b,c))
        graph.append((b,a,c))
    for i in range(w):
        a,b,c=map(int,input().split())
        graph.append((a,b,-c))
    check=func(1)
    if check==True:
        print("YES") 
    else:
        print("NO")
    