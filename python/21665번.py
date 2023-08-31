N,M=map(int,input().split())
li=[]
for i in range(N):
    tmp=''
    for i in input().strip():
        if i=='W':tmp+='B'
        else:tmp+='W'
    li.append(tmp)
res=0
input()
for i in range(N):
    tmp=input()
    for j in range(M):
        if tmp[j]!=li[i][j]:res+=1
print(res)
