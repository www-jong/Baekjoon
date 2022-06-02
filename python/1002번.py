import sys
for i in range(int(sys.stdin.readline())):
    ans=0
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    pp=((abs(x2-x1)**2)+(abs(y2-y1)**2))**0.5 # 두점사이거리
    ptop=r1+r2 # 교점과 각 점 사이의거리합
    if pp<ptop: 
        if (x1==x2)and(y1==y2):
            if r1==r2:
                ans=-1
            else:ans=0
        else:
            if (pp+(r1 if r1<r2 else r2))==(r1 if r1>r2 else r2): 
                ans=1
            elif (pp+(r1 if r1<r2 else r2))<(r1 if r1>r2 else r2):
                ans=0
            else:ans=2
    elif pp==ptop:
        ans=1
    elif pp>ptop:
        ans=0
    elif (x1==x2)and(y1==y2):
        if r1==r2:
            ans=-1
        else:ans=0
    print(ans)
            