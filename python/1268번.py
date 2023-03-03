N=int(input())
li=[]
res=[0,0]
dic={}

for i in range(N):
    li.append(list(map(int,input().split())))
    dic[i]=0
for i in range(N):
    for j in range(5):
        for k in range(N):
            if li[i][j]==li[k][j]:
                dic[i]+=1
for i in range(N):
    if dic[i]>res[0]:
        res=dic[i],i
print(res[1]+1)