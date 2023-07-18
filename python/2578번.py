li=[[0]]
dic={}
res=0
checks=[[1,5],[2,4],[3,3],[4,2],[5,1]]
def check(x,y):
    ttmp=0
    xvers=0
    yvers=0
    svers1=0
    svers2=0
    for i in range(1,6):
        if li[x][i]==0:
            xvers+=1
        if li[i][y]==0:
            yvers+=1
        if x==y and li[i][i]==0:
            svers1+=1
        if [x,y] in checks and li[6-i][i]==0:
            svers2+=1
    if xvers==5:
        ttmp+=1
    if yvers==5:
        ttmp+=1
    if svers1==5:
        ttmp+=1
    if svers2==5:
        ttmp+=1
    return ttmp
    
for i in range(1,6):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,6):
        dic[tmp[j]]=[i,j]
    li.append(tmp)

bingo=[]
for i in range(5):
    bingo.extend(list(map(int,input().split())))
for i in range(25):
    x,y=dic[bingo[i]]
    li[x][y]=0
    ttt=check(x,y)
    res+=ttt
    print(f'now : {bingo[i]}, {x}:{y} -> {ttt}')
    if res>=3:
        print(i+1)
        break
for i in range(1,6):
    print(li[i])