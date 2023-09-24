from collections import deque
D=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
for i in range(int(input())):
    li=[input().split() for i in range(3)]
    v=[0]*512
    b=''
    for x in range(3):
        for y in range(3):
            b+='1' if li[x][y]=='T' else '0'

    q=deque()
    q.append((b,1))
    v[int(b,2)]=1
    while q:
        r,c=q.popleft()
        for i in D:
            t=r
            for k in i:
                t=t[:k]+('0'if r[k]=='1' else '1')+t[k+1:]
            if not v[int(t,2)] or v[int(t,2)]>c+1:
                v[int(t,2)]=c+1
                q.append((t,c+1))
    if v[511]==0 and v[0]==0:
        print(-1)
    else:
        if v[511]==0:v[511]=1000
        if v[0]==0:v[0]=1000
        print(min(v[511],v[0])-1)