import heapq
import sys
input=sys.stdin.readline
INF=10**9
def dstra(start):
    q=[]
    #시작노드로 가기위한 최단경로는 0으로 서정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance=[INF]*(n+1)
    distance[start]=0
    while q:
        #가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost=dist+i[1]
            #현재 노드를 거쳐, 다른노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

for _ in range(int(input())):

    #노드의 개수, 도로의개수 입력
    n,m=map(int,input().split())

    graph=[[] for i in range(n+1)]
    #최단거리 테이블을 모드 무한으로 초기화
    distance=[INF]*(n+1)
    for i in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    _=int(input())
    friends=list(map(int,input().split()))
    res=10**9
    rest=-1
    for A in range(1,n+1):
        t=dstra(A)
        tmps=sum([t[i] for i in range(1,n+1) if i in friends])
        if tmps<res:
            rest=A
        res=min(res,tmps)
    print(rest)