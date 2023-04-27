from collections import deque
import sys
sys.setrecursionlimit(10**9)
maps=['aaaaaa']
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for i in range(5):
    maps.append('a'+input())
res=0
dep=[]
def func(now,s,im):
    global dep
    if im>=4:
        return
    if len(now)==7:
        if check(now):
            count(now)
        return
    for i in range(s+1,26):
        r=i//5+(0 if i%5==0 else 1)
        c=i%5+(5 if i%5==0 else 0)
        now.append([r,c])
        func(now,i,im+1 if maps[r][c]=='Y' else im)
        now.pop()

def check(now):
    tmp_visit=[[0]*(6) for i in range(6)]
    q=deque()
    q.append((now[0][0],now[0][1]))
    tmp_visit[now[0][0]][now[0][1]]=1
    cc=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=5 and 1<=ny<=5:
                if not tmp_visit[nx][ny] and [nx,ny] in now:
                    cc+=1
                    tmp_visit[nx][ny]=1
                    q.append((nx,ny))
    if cc!=7:
        return False
    return True
def count(now):
    global res
    queens=0
    for x,y in now:
        if maps[x][y]=='S':
            queens+=1
        if queens>=4:
            res+=1
            break
func([],0,0)
print(res)