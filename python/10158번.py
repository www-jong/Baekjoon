w,h=map(int,input().split())
x,y=map(int,input().split())
dx=[1,-1,-1,1] #오른위, 왼위, 왼아래, 오른아래
dy=[1,1,-1,-1]
t=int(input())
first_loc=[x,y]
check=0
idx=0
i=1
while i<=t:
    if idx==4:idx=0
    if idx==5:idx=1
    elif idx==-1:idx=3
    elif idx==-2:idx=2
    nx=x+dx[idx]
    ny=y+dy[idx]

    if (nx==0 and ny==h)or(nx==0 and ny==0)or(nx==w and ny==0)or(ny==w and ny==h):
        idx+=2
    
    else:
        if nx==0:
            if idx==1:
                idx-=1
            elif idx==2:
                idx+=1
        elif nx==w:
            if idx==0:
                idx+=1
            elif idx==3:
                idx-=1
        
        if ny==0:
            if idx==2:
                idx-=1
            elif idx==3:
                idx+=1
        if ny==h:
            if idx==0:
                idx-=1
            elif idx==1:
                idx+=1
    if [nx,ny]==first_loc and check==0 and idx==0 and i!=1:
        print(f'now : {i} , {t%i}')
        check=1
        i=t-t%i
    i+=1
    x=nx
    y=ny

print(x, y)