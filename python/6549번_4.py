import sys
# 단순 분할정복, 시간초과:메모리초과
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

def func(start,end):
    global res
    if start==end or start==end-1:
        return
    tmp=[10**11,[]]
    for i in range(start+1,end):
        if li[i]<tmp[0]:
            tmp=[li[i],[i]]
        elif li[i]==tmp[0]:
            tmp[1].append(i)
    res=max(res,tmp[0]*(end-start-1))
    tmp[1].append(end)
    func(start,tmp[1][0])
    for i in range(len(tmp[1])-1):
        func(tmp[1][i],tmp[1][i+1])

while True:
    li=list(map(int,input().split()))
    res=0
    if li[0]==0:break
    else:li.pop(0)
    func(-1,len(li))
    print(res)