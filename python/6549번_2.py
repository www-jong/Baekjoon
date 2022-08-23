import sys

while True:
    li=list(map(int,sys.stdin.readline().rstrip().split()))
    if li[0]==0:
        break
    li.pop(0)
    tmp=li[0]
    tmpheight=li[0]
    end=0
    n,m=len(li),0
    tmpst=0
    tmpend=0
    for st in range(n):
        while tmp<m and end<n:
            if tmpheight<li[end]:
                tmpheight=li[end]
            tmp=tmpheight*(end-st+1)
            end+=1
        if tmp>m:
            m=tmp
            tmpst=st
            tmpend=end
        print("start : %d, end : %d"%(st,end))
        if end-(st+1)>=1:
            ttmin=min(min(li[st+1:end]),li[st])
        else:
            ttmin=li[len(li)-1 if end==len(li) else end]
        if li[st]<ttmin:
            tmpheight=ttmin
            tmp=tmpheight*(end-st+1)
        else:
            tmp-=tmpheight
    print("%d %d %d"%(m,tmpst,tmpend))

'''
투포인터로 각 구간의 합(구간의길이*구간에서 가장 작은값)을 구한다
'''