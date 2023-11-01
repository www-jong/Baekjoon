N,L=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
li2=[[li[j][i]for j in range(N)] for i in range(N)]
r=0
for i in range(N):
    plag=True
    before=li[i][0]
    visit=[0]*N
    for j in range(N):
        if abs(before-li[i][j])>=2:
            plag=False
            break
        elif li[i][j]-before==1:
            if j-L<0:
                plag=False
                break
            if li[i][j-L:j].count(before)<L or(sum(visit[j-L:j])):
                plag=False
                break
            else:
                for k in range(j-L,j):
                    visit[k]=1
        elif before-li[i][j]==1:
            if j+L>N:
                plag=False
                break
            if li[i][j:j+L].count(li[i][j])<L or sum(visit[j:j+L]):
                plag=False
                break
            else:
                for k in range(j,j+L):
                    visit[k]=1
        before=li[i][j]
    if plag:
        r+=1
        print('!',i)
for i in range(N):
    plag=True
    before=li2[i][0]
    visit=[0]*N
    for j in range(N):
        if abs(before-li2[i][j])>=2:
            plag=False
            break
        elif li2[i][j]-before==1:
            if j-L<0:
                plag=False
                break
            if li2[i][j-L:j].count(before)<L or(sum(visit[j-L:j])):
                plag=False
                break
            else:
                for k in range(j-L,j):
                    visit[k]=1
        elif before-li2[i][j]==1:
            if j+L>N:
                plag=False
                break
            if li2[i][j:j+L].count(li2[i][j])<L or sum(visit[j:j+L]):
                plag=False
                break
            else:
                for k in range(j,j+L):
                    visit[k]=1
        before=li2[i][j]
    if plag:
        r+=1
        print(i)
print(r)
