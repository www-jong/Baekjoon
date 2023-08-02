N,M,B=map(int,input().split())
def get_idx(height):
    start,end=0,N*M
    mid=(start+end)//2
    ii=0
    while start<end:
        if li[mid]==height:
            tmp=li[mid]
            while li[mid]==tmp:
                mid+=1
            return mid
        elif li[mid]<height:
            start=mid
        else:
            end=mid+1
        ii+=1
        if ii>=18:
            if li[mid]<height:
                tmp=li[mid]
                while li[mid]<=height:
                    mid+=1
                return mid
            else:
                tmp=li[mid]
                while li[mid]==tmp:
                    mid+=1
                return mid

li=[]
res=[10**10,0]
for i in range(N):
    li.extend(list(map(int,input().split())))
li.sort()
all_block=sum(li)
low=min(li)
high=max(li)
idx=0
for i in range(low,high+1):
    while li[idx]<=i:
        idx+=1
        if idx==N*M:break
    dig_block=sum(li[idx:])-(N*M-idx)*i
    add_block=idx*i-sum(li[:idx])
    if dig_block+B<add_block:
        continue
    else:
        if res[0]>=dig_block*2+add_block:
            res=[dig_block*2+add_block,i]
        elif res[0]<dig_block*2+add_block:
            break
print(*res)