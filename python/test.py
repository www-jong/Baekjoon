import sys
sys.setrecursionlimit(10000000)
'''
def func(st,end):
    
    if end-st>3:
        mid=(st+end)//2
        mid_val=(end-st)//2
        func(st,st+mid_val//2)
        func(st+mid_val//2+1,mid)
        func(mid+1,st+(mid_val+1)*3//2-1)
        func(st+(mid_val+1)*3//2,end)
    else:
        print(f'{st}-{end}')
'''

def func(st,end,x,y,n):
    
    if end-st>3:
        mid=(st+end)//2
        mid_val=(end-st)//2
        func(st,st+mid_val//2 , x , y,n-1)
        func(st+mid_val//2+1,mid , x,y+ 2**(n),n-1)
        func(mid+1,st+(mid_val+1)*3//2-1 ,x+2**(n) ,y ,n-1)
        func(st+(mid_val+1)*3//2,end ,x+2**(n) ,y+2**(n) ,n-1)
    else:
        print(f'{st}-{end} || {x}-{y}')

n=3
func(0,63,0,0,n-1)

def funcs(st,end):
    mid=(st+end)//2
    mid_val=(end-st)//2
    print(f'{st} : {st+mid_val//2}')
    print(f'{st+mid_val//2+1} : {mid}')
    print(f'{mid+1} : {st+(mid_val+1)*3//2-1}')
    print(f'{st+(mid_val+1)*3//2} : {end}')

#funcs(16,31)
#for i in range(2,12,2):
#    print(f'2**{i} -> {2**i-1}')
#    funcs(0,2**i-1)
