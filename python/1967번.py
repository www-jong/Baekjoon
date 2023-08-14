# 무조건 이진트리가 아니다. 
'''
반례
5
1 2 3
1 3 4
1 4 5
1 5 6
'''
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def func(x):
    global res
    left_val,right_val=0,0
    if left_tree[x][0]!=0:
        left_val=func(left_tree[x][0])+left_tree[x][1]
    if right_tree[x][0]!=0:
        right_val=func(right_tree[x][0])+right_tree[x][1]
    #print(x,left_val,right_val)
    res=max(res,left_val,right_val,left_val+right_val)
    return max(left_val,right_val)

n=int(input())
check=[0]*(n+1)
check[0]=1
left_tree=[[0,0] for i in range(n+1)]
right_tree=[[0,0] for i in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    check[b]=1
    if left_tree[a][0]==0:
        left_tree[a]=[b,c]
    else:
        right_tree[a]=[b,c]
res=0
for i in range(1,n+1):
    if check[i]==0:
        func(i)
        break
print(res)