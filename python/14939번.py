from copy import deepcopy
li=[]
d=[0,0,0,1,-1]
res=101
for i in range(10):
    tmp=input()
    t=[]
    for j in range(10):
        if tmp[j]=='O':
            t.append(1)
        else:
            t.append(0)
    li.append(t)

for i in range(1024):
    tmpli=deepcopy(li)
    co=0
    for j in range(10):
        if i&1<<j:
            co+=1
            for k in range(5):
                nx=0+d[k]
                ny=j+d[4-k]
                if 0<=nx<10 and 0<=ny<10:
                    tmpli[nx][ny]=not tmpli[nx][ny]

    for x in range(1,10):
        for y in range(10):
            if tmpli[x-1][y]:
                co+=1
                for k in range(5):
                    nx=x+d[k]
                    ny=y+d[4-k]
                    if 0<=nx<10 and 0<=ny<10:
                        tmpli[nx][ny]= not tmpli[nx][ny]
    if not sum(tmpli[-1]):
        res=min(res,co)
print(res if res!=101 else -1)