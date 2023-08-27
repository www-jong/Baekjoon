import sys
input=sys.stdin.readline
idx=1
while True:
    res=0
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    graph=[[] for i in range(N+1)]
    visit=[0]*(N+1)
    for i in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,N+1):
        if not visit[i]:
            q=[]
            res+=1
            #print(f'!{i}')
            q.append((i,0))
            visit[i]=0
            plag=0
            while q:
                x,before_node=q.pop()
                for node in graph[x]:
                    if node==before_node:
                        continue
                    if not visit[node]:
                        #print(f'방문 {node}')
                        visit[node]=1
                        q.append((node,x))
                    else:
                        res-=1
                        plag=1
                        break
                if plag:
                    break
    #print(res)
    #print(graph)
    if res==0:
        print(f'Case {idx}: No trees.')
    elif res==1:
        print(f'Case {idx}: There is one tree.')
    else:
        print(f'Case {idx}: A forest of {res} trees.')
    idx+=1