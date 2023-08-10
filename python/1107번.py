import sys
sys.setrecursionlimit(100000)
def func(v,idx):
    global res
    if v:
        if abs(int(v)-int(N))+len(v)<res:
            res=abs(int(v)-int(N))+len(v)
    if idx>=len(N)+2:
        return

    for i in button:
        func(v+str(i),idx+1)

N=input()
M=int(input())
if M!=0:
    M_li=list(map(int,input().split()))
    button=[i for i in range(10) if i not in M_li]
else:
    button=[i for i in range(10)]
res=int(N)-100 if int(N)>100 else 100-int(N)
func('',0)
print(res)