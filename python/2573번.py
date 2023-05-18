import sys
from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

N,M=map(int,input().split())

li=[[0]*(M+1)]
for i in range(N):
    li.append([0]+list(map(int,input().split())))

def check():
    res=0
    visit=[[0]*(M+1) for i in range(N+1)]
    checker=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if li[i][j]!=0:
                checker=1
            if visit[i][j]!=0 or li[i][j]==0:
                continue
            q=deque()
            q.append((i,j))
            visit[i][j]=1
            res+=1
            while q:
                x,y=q.popleft()
                for z in range(4):
                    nx=x+dx[z]
                    ny=y+dy[z]
                    if 1<=nx<=N and 1<=ny<=M:
                        if visit[nx][ny]==0 and li[nx][ny]!=0:
                            visit[nx][ny]=1
                            q.append((nx,ny))
    return res,checker

def melt():
    global li
    tmp=[]
    for i in range(1,N+1):
        for j in range(1,M+1):
            if li[i][j]!=0:
                ch=0
                for z in range(4):
                    nx=i+dx[z]
                    ny=j+dy[z]
                    if 1<=nx<=N and 1<=ny<=M:
                        if li[nx][ny]==0:
                            ch+=1
                if ch!=0:
                    tmp.append((i,j,ch))
    for i,j,c in tmp:
        li[i][j]=max(li[i][j]-c,0)
mres=1
now,chk=check()
if now>=2 or chk==0:
    print(0)
else:
    while True:
        melt()
        now,chk=check()
        if chk==0:
            print(0)
            break
        if now>=2:
            print(mres)
            break
        mres+=1