from copy import deepcopy
N=int(input())
li=[[0]]
res=0
def up(li):
    for i in range(1,N+1):
        j=1
        while j<N:
            if j<N:
                if li[j][i]==0:
                    ch=0
                    for k in range(j+1,N+1):
                        if li[k][i]!=0 or ch==1:
                            li[k-1][i],li[k][i]=li[k][i],0
                            ch=1
                    if ch==1:
                        j-=1
                elif li[j][i]==li[j+1][i]:
                    li[j][i],li[j+1][i]=li[j][i]*2,0
            j+=1
    return li

def down(li):
    for i in range(1,N+1):
        j=N
        while j>1:
            if li[j][i]==0:
                ch=0
                for k in range(j-1,0,-1):
                    if li[k][i]!=0 or ch==1:
                        li[k+1][i],li[k][i]=li[k][i],0
                        ch=1
                if ch==1:
                    j+=1
            elif li[j][i]==li[j-1][i]:
                li[j][i],li[j-1][i]=li[j][i]*2,0
            j-=1
    return li

def left(li):
    for i in range(1,N+1):
        j=1
        while j<N:
            if j<N:
                if li[i][j]==0:
                    ch=0
                    for k in range(j+1,N+1):
                        if li[i][k]!=0 or ch==1:
                            li[i][k-1],li[i][k]=li[i][k],0
                            ch=1
                    if ch==1:
                        j-=1
                elif li[i][j]==li[i][j+1]:
                    li[i][j],li[i][j+1]=li[i][j+1]*2,0
            j+=1
    return li

def right(li):
    for i in range(1,N+1):
        j=N
        while j>1:
            if li[i][j]==0:
                ch=0
                for k in range(j-1,0,-1):
                    if li[i][k]!=0 or ch==1:
                        li[i][k+1],li[i][k]=li[i][k],0
                        ch=1
                if ch==1:
                    j+=1
            elif li[i][j]==li[i][j-1]:
                li[i][j],li[i][j-1]=li[i][j]*2,0
            j-=1
    return li

for i in range(N):
    li.append([0]+list(map(int,input().split())))

def dfs(li,count):
    global res
    #for i in range(1,N+1):
    #    print(*li[i][1:])
    if count==5:
        for i in range(1,N+1):
            for j in range(1,N+1):
                res=max(res,li[i][j])
        return
    
    dfs(up(deepcopy(li)),count+1)
    dfs(down(deepcopy(li)),count+1)
    dfs(left(deepcopy(li)),count+1)
    dfs(right(deepcopy(li)),count+1)
    
dfs(li,0)
print(res)
#print(tes)
'''
tmpli=deepcopy(li)
tmpli=left(tmpli)
for i in range(1,N+1):
    print(*tmpli[i][1:])
print('----')
tmpli=up(tmpli)
for i in range(1,N+1):
    print(*tmpli[i][1:])
print('----')
tmpli=left(tmpli)
for i in range(1,N+1):
    print(*tmpli[i][1:])
print('----')
tmpli=down(tmpli)
for i in range(1,N+1):
    print(*tmpli[i][1:])
print('----')
tmpli=left(tmpli)
for i in range(1,N+1):
    print(*tmpli[i][1:])

for i in up(deepcopy(li)):
    print(*i[1:])
for i in down(deepcopy(li)):
    print(*i[1:])
for i in left(deepcopy(li)):
    print(*i[1:])
for i in right(deepcopy(li)):
    print(*i[1:])

4
2 2 2 2
2 4 2 4
4 4 2 4
8 8 2 8

'''
