from collections import deque
import sys,math
input=sys.stdin.readline
N,M,k=map(int,input().split())
graph=[[0]*(N+1) for i in range(N+1)]
move=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
balls={}
def dicsum(a,b):
    print(a)
    print(b)
    print(a[0]+b[0])
    for i in range(4):
        a[i]+=b[i]
    return a
def func1(balls):
    newballs={}
    for (x,y),(m,s,d,i) in balls.items():
        x= 1 if (x+s*move[d][0])%N==0 else (x+s*move[d][0])%N
        y= 1 if (y+s*move[d][1])%N==0 else (y+s*move[d][1])%N
        if (x,y) in newballs:
            if (newballs[(x,y)][2]==1 and d%2==0) or (newballs[(x,y)][2]==2 and d%2==1):
                newballs[(x,y)]=dicsum(newballs[(x,y)],[m,s,-10000,i])
            else:
                newballs[(x,y)]=dicsum(newballs[(x,y)],[m,s,-10000,i])
        else:
            if d%2==0:
                newballs[(x,y)]=[m,s,2,i]
            elif d%2==1:
                newballs[(x,y)]=[m,s,1,i]
    print('yes')
    return newballs

def func2(balls):
    newballs={}
    for (x,y),(m,s,d,i) in balls.items():
        s=math.floor(s/i)
        m=math.floor(m/5)
        if m==0:
            continue
        if i>=2:
            if d>0:
                for j in [0,2,4,6]:
                    newballs[(x,y)]=[m,s,j,1]
            else:
                for j in [1,3,5,7]:
                    newballs[(x,y)]=[m,s,j,1]
    return newballs

for i in range(M):
    r,c,m,s,d=map(int,input().split())
    balls[(r,c)]=[m,s,d,1]

for i in range(k):
    if len(balls)!=0:
        balls=func1(balls)
    if len(balls)!=0:
        print(balls.items())
        balls=func2(balls)

ans=0
for i,_,_,_ in balls.values():
    ans+=i
print(ans)
print(balls.items())
