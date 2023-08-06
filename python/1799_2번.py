# 시간초과
N=int(input())
li=[]
res1,res2=0,0
def updates(x,y):
    d1={}
    for i in range(-N,N+1):
        if 0<=x+i<N and 0<=y+i<N:
            if (x+i,y+i) not in d1:d1[(x+i,y+i)]=1
        if 0<=x+i<N and 0<=y-i<N:
            if (x+i,y-i) not in d1:d1[(x+i,y-i)]=1
    return d1

def func(x,y,dic_check,count,types):
    global res1,res2,ch
    if y>=N:
        x+=1
        if N%2==0:
            y=1 if y==N else 0
        else:
            y-=N

    if x==N or len(dic_check)>=(N*N)//2+(0 if N%2==0 else types):
        #print(f't:{types}, {count} {dic_check}')
        if types:
            res1=max(res1,count)
        else:
            res2=max(res2,count)
        ch+=1
        return
    if (x,y) not in dic_check:
        tmp_check=updates(x,y)
        tmp_check.update(dic_check)
        func(x,y+2,tmp_check,count+1,types)

    func(x,y+2,dic_check,count,types)
dic1,dic2={},{}
ch=0
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(N):
        if tmp[j]==0:
            if (i+j)%2==0:
                dic1[(i,j)]=1
            else:
                dic2[(i,j)]=1
    li.append(tmp)

func(0,0,dic1,0,1)
func(0,1,dic2,0,0)
print(res1+res2)
print(ch)