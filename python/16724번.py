N,M=map(int,input().split())
li=[[0]]
for i in range(N):
    li.append('0'+input())
dic={'D':[1,0],'U':[-1,0],'R':[0,1],'L':[0,-1]}
res=0
visit=[[0]*(M+1) for i in range(N+1)]
ch={}
def dfs(x,y,val):
    global res,visit,ch
    visit[x][y]=val

    nx,ny=dic[li[x][y]][0]+x,dic[li[x][y]][1]+y
    if visit[nx][ny]==0:
        ch[str(nx)+' '+str(ny)]=1
        dfs(nx,ny,val)
    else:
        return [nx,ny]


for i in range(1,N+1):
    for j in range(1,M+1):
        if visit[i][j]==0:
            ch[str(i)+' '+str(j)]=1
            s=dfs(i,j,1)
            if s:
                if str(s[0])+' '+str(s[1]) not in ch:
                    res+=1
print(res)