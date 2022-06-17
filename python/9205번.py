from collections import deque
t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def adds(n):
    return int(n)+32768
for i in range(t):
    n=int(input())
    home=list(map(adds,input().split()))+[0]
    beers=[]
    for i in range(1,n+1):
        beers.append(list(map(adds,input().split()))+[i])
    end=list(map(adds,input().split()))
    q=deque()
    check=0
    q.append((home[0],home[1],home[2]))
    visit=[0]*(n+1)
    while q:
        nx,ny,num=q.popleft()
        if abs(nx-end[0])+abs(ny-end[1])<=1000:
            check=1
            break
        beers.sort(key=lambda x:abs(x[0]-nx)+(abs(x[1]-ny)))
        for j in range(len(beers)):
            if abs(beers[j][0]-nx)+abs(beers[j][1]-ny)<=1000 and visit[beers[j][2]]==0:
                visit[beers[j][2]]=1
                q.append(beers[j])
    print("happy" if check==1 else "sad")