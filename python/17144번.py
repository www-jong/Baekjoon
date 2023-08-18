import copy
R,C,T=map(int,input().split())
d=[0,0,1,-1]
dust={}
li=[]
air=[]
for i in range(R):
    tmp=list(map(int,input().split()))
    for j in range(C):
        if tmp[j]==-1:
            air.append((i,j))
    li.append(tmp)
air.sort(key=lambda x:x[0])
for i in range(T):
    tmp_li=[[0]*C for i in range(R)]
    for x in range(R):
        for y in range(C):
            if (x,y) in air:
                continue
            v=li[x][y]
            c=0
            for n in range(4):
                nx=x+d[n]
                ny=y+d[3-n]
                if 0<=nx<R and 0<=ny<C and (nx,ny) not in air:
                    tmp_li[nx][ny]+=v//5
                    c+=v//5
            tmp_li[x][y]+=v-c
    for i in range(air[0][0]):
        tmp_li[i+1][0]=tmp_li[i][0]
    tmp_li[air[0][0]][air[0][1]]=0
    for i in range(C-1):
        tmp_li[0][i]=tmp_li[0][i+1]
    for i in range(air[0][0]):
        tmp_li[i][-1]=tmp_li[i+1][-1]
    for i in range(C-1,0,-1):
        tmp_li[air[0][0]][i]=tmp_li[air[0][0]][i-1]

    for i in range(air[1][0],R-1):
        tmp_li[i][0]=tmp_li[i+1][0]
    tmp_li[air[1][0]][0]=0
    for i in range(C-1):
        tmp_li[R-1][i]=tmp_li[R-1][i+1]
    for i in range(R-1,air[1][0]-1,-1):
        tmp_li[i][-1]=tmp_li[i-1][-1]
    for i in range(C-1,0,-1):
        tmp_li[air[1][0]][i]=tmp_li[air[1][0]][i-1]
    li=copy.deepcopy(tmp_li)
res=0
print(li)
for i in range(R):
    print(li[i])
    res+=sum(li[i])
print(res)