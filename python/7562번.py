from collections import deque
dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,1,-1]
for i in range(int(input())):
    n=int(input())
    start=list(map(int,input().split()))
    end=list(map(int,input().split()))
    visit=[[0]*n for i in range(n)]
    res=1000000
    if start==end:
        print(0)
    else:
        q=deque()
        q.append((start[0],start[1],1))
        visit[start[0]][start[1]]=1
        while q:
            x,y,z=q.popleft()
            for i in range(8):
                sx=x+dx[i]
                sy=y+dy[i]
                if 0<=sx<n and 0<=sy<n and visit[sx][sy]!=1:
                    if [sx,sy]==end:
                        res=z
                        q.clear()
                        break
                    q.append((sx,sy,z+1))
                    visit[sx][sy]=1
        print(res)