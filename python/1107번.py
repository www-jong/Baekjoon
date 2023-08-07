import sys
sys.setrecursionlimit(1000000)
def func(v,idx):
    global gap
    if v:
        if abs(int(v)-int(N))<gap[0]:
            gap=[abs(int(v)-int(N)),v]
        elif abs(int(v)-int(N))==gap[0]:
            if len(v)<gap[0]:
                gap=[abs(int(v)-int(N)),v]
    if idx==len(N)+1:
        return
    for i in ri:
        func(v+str(i),idx+1)
N=input()
M=int(input())

gap=[10**7,0]
ri=[i for i in range(10)]
if M!=0:
    for i in list(map(int,input().split())):
        ri.remove(i)
func('',0)
if gap[0]==0:
    print(len(N))
else:
    print(min(gap[0]+len(gap[1]),abs(int(N)-100)))
print(gap)