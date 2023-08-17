import sys
sys.setrecursionlimit(1000000)
dx,dy=[0,0,-1,1],[1,-1,0,0] #동 서 북 남
dice=[0,0,0,0,0,0]#정면 위 오른 왼 아래 바닥
def left(dice):
    dice[0],dice[2],dice[3],dice[5]=dice[2],dice[5],dice[0],dice[3]
    return dice
def right(dice):
    dice[0],dice[2],dice[3],dice[5]=dice[3],dice[0],dice[5],dice[2]
    return dice
def up(dice):
    dice[0],dice[1],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[1]
    return dice
def down(dice):
    dice[0],dice[1],dice[4],dice[5]=dice[1],dice[5],dice[0],dice[4]
    return dice
move={0:right,1:left,2:up,3:down}
N,M,x,y,K=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]
order=list(map(int,input().split()))
for i in order:
    nx=x+dx[i-1]
    ny=y+dy[i-1]
    if 0<=nx<N and 0<=ny<M:
        dice=move[i-1](dice)
        if li[nx][ny]!=0:
            dice[5]=li[nx][ny]
            li[nx][ny]=0
        else:
            li[nx][ny]=dice[5]
        print(dice[0])
        x,y=nx,ny