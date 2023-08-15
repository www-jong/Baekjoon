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
    tmp_vals=[]
    for idx,v in tree[x]:
        tmp_vals.append(func(idx)+v)
    tmp_vals.sort(reverse=True)
    if tmp_vals:
        res=max(res,tmp_vals[0]+(tmp_vals[1] if len(tmp_vals)>=2 else 0))
        return tmp_vals[0]
    else:
        return 0
n=int(input())
check=[0]*(n+1)
check[0]=1

tree=[[] for i in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    check[b]=1
    tree[a].append([b,c])

res=0
for i in range(1,n+1):
    if check[i]==0:
        func(i)
        break
print(res)