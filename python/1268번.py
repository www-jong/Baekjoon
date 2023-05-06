N=int(input())
dic={}
li=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(5):
        if str(j)+str(tmp[j]) not in dic:
            dic[str(j)+str(tmp[j])]=set([i])
        else:
            dic[str(j)+str(tmp[j])].add(i)
    li.append(tmp)
res=[-1,0]
for i in range(len(li)):
    tmps=set([])
    for j in range(5):
        tmps=tmps.union(dic[str(j)+str(li[i][j])])
    if len(tmps)>res[0]:
        res=[len(tmps),i]
print(res[1]+1)