import heapq
import sys
aaaa=int(input())
INF=int(1e9)


def dijkstra(s):
    q=[]
    #시작노드로 가기위한 최단경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,s))
    distance=[INF]*(n+1)
    distance[s]=0
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

for _ in range(aaaa):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph=[[] for i in range(n+1)]

    res=[]
    end_list=[]
    #모든 간선정보 입력
    for _ in range(m):
        a,b,c=map(int,input().split())
        #a->b 비용이 c라는 의미
        graph[a].append((b,c))
        graph[b].append((a,c))
    dis_s_to=dijkstra(s)
    dis_g_to=dijkstra(g)
    dis_h_to=dijkstra(h)
    for _ in range(t):
        endpoint=int(input())
        if dis_s_to[endpoint]!=INF:
          if (dis_s_to[endpoint]==dis_s_to[g]+dis_g_to[h]+dis_h_to[endpoint]) or (dis_s_to[endpoint]==dis_s_to[h]+dis_h_to[g]+dis_g_to[endpoint]):
             res.append(endpoint)  
    res.sort()
    print(*res,sep=" ")



