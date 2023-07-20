N,r,c=map(int,input().split())

def func(st,end,x,y,n):
    if x<=r<=x+2**(n+1) and y<=c<=y+2**(n+1):
        if end-st>3:
            mid=(st+end)//2
            mid_val=(end-st)//2
            func(st,st+mid_val//2 , x , y,n-1)
            func(st+mid_val//2+1,mid , x,y+ 2**(n),n-1)
            func(mid+1,st+(mid_val+1)*3//2-1 ,x+2**(n) ,y ,n-1)
            func(st+(mid_val+1)*3//2,end ,x+2**(n) ,y+2**(n) ,n-1)
        if n==0 and x<=r<=x+1 and y<=c<=y+1:
            print(f'{st+(c-y)+(r-x)*2}')
func(0,2**(N*2)-1,0,0,N-1)