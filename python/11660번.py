import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graphx=[[0]*(n+1) for i in range(n+1)]
graphall=[[0]*(n+1) for i in range(n+1)]
for i in range(n):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,len(tmp)):
        graphx[i+1][j]=graphx[i][j]+tmp[j]
        
        graphall[i+1][j]=graphall[i+1][j-1]+tmp[j]+graphx[i][j]
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    sum=graphall[x2][y2]+graphall[x1-1][y1-1]
    sum-=graphall[x2][y1-1]+graphall[x1-1][y2]
    print(sum)