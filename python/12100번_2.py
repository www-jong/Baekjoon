from copy import deepcopy
N=int(input())
li=[[0]]
res=0
def up(li):
    for i in range(1,N+1):
        poi=1
        for j in range(1,N+1):
            if li[j][i]:
                tmp,li[j][i]=li[j][i],0
                if li[poi][i]==0: # 포인터위치값이 0인경우
                    li[poi][i]=tmp
                elif li[poi][i]==tmp: #포인터위치값이 현재값과 같을경우 
                    li[poi][i]*=2
                    poi+=1
                else:
                    poi+=1
                    li[poi][i]=tmp
    return li

def down(li):
    for i in range(1,N+1):
        poi=N
        for j in range(N,0,-1):
            if li[j][i]:
                tmp,li[j][i]=li[j][i],0
                if li[poi][i]==0: # 포인터위치가 0인경우
                    li[poi][i]=tmp
                elif li[poi][i]==tmp:
                    li[poi][i]*=2
                    poi-=1
                else:
                    poi-=1
                    li[poi][i]=tmp
    return li

def left(li):
    for i in range(1,N+1):
        poi=N
        for j in range(N,0,-1):
            if li[i][j]:
                tmp,li[i][j]=li[i][j],0
                if li[i][poi]==0: # 포인터위치가 0인경우
                    li[i][poi]=tmp
                elif li[i][poi]==tmp:
                    li[i][poi]*=2
                    poi-=1
                else:
                    poi-=1
                    li[i][poi]=tmp
    return li

def right(li):
    for i in range(1,N+1):
        poi=1
        for j in range(1,N+1):
            if li[i][j]:
                tmp,li[i][j]=li[i][j],0
                if li[i][poi]==0: # 포인터위치가 0인경우
                    li[i][poi]=tmp
                elif li[i][poi]==tmp:
                    li[i][poi]*=2
                    poi+=1
                else:
                    poi+=1
                    li[i][poi]=tmp
    return li

for i in range(N):
    li.append([0]+list(map(int,input().split())))

def dfs(li,count):
    global res
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