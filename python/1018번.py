n,m=map(int,input().split())
w='WB'
b='BW'
ww=w*25
bb=b*25
www=[]
bbb=[]
for i in range(50):
    if i%2==0:
        www+=[ww]
        bbb+=[bb]
    else:
        www+=[bb]
        bbb+=[ww]
ans=[]
for i in range(m):
    ans+=[input()]
an=[]
res=0
for i in range(len(ans)):
    if ans[0][0]=="W":
        an=www
    else:
        an=bbb
    for j in range(len(ans[0])):
        if ans[i][j]!=an[i][j]:
            res+=1
print(res)