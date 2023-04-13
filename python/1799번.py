
N=int(input())
oli=[[0]*(N+1)]
dics={'0,'+str(N):1}
for i in range(1,N+1):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,N+1):
        if tmp[j]==0:
            dics[str(i)+","+str(j)]=1
    oli.append(tmp)
dx=[1,1,-1,-1]
dy=[-1,1,-1,1]
res=0
def colors(x,y):
    tmpdic={}
    for i in range(4):
        for j in range(N+1):
            nx=x+dx[i]*j
            ny=y+dy[i]*j
            if 1<=nx<=N and 1<=ny<=N:
                if str(nx)+","+str(ny) not in tmpdic:
                    tmpdic[str(nx)+","+str(ny)]=1
                #print(f' blocked! {nx}:{ny} in {x}:{y}')
            else:
                break
    return tmpdic

t=0
def func(x,y,dic,now):
    global res,t
    t+=1
    if x==N+1 and y==1:
        res=max(res,now)
        return
    #print(f'{x}:{y}, {dic}')
    if str(x)+","+str(y) not in dic:
        #print(f' now go {x}:{y}')
        new_dic=colors(x,y)
        func(x+1 if y==N else x,1 if y==N else y+1,dict(new_dic,**dic),now+1)
    func(x+1 if y==N else x,1 if y==N else y+1,dic,now)    
func(0,N,dics,0)
print(res)
print(t)