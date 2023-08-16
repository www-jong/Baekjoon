import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
li=[]
while True:
    try:
        x=int(input())
        li.append(x)
    except:
        break
def func(tmp):
    if len(tmp)==0:return
    mid=tmp[0]
    ltree=[]
    rtree=[]
    for i in range(1,len(tmp)):
        if tmp[i]>mid:
            ltree=tmp[1:i]
            rtree=tmp[i:]
            break
    else:
        ltree=tmp[1:]

    func(ltree)
    func(rtree)
    print(mid)

func(li)