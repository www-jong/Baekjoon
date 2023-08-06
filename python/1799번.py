# 시간초과
N=int(input())
li=[]
res=0
def updates(x,y):
    d1={}
    for i in range(-N,N+1):
        if 0<=x+i<N and 0<=y+i<N:
            if (x+i,y+i) not in d1:d1[(x+i,y+i)]=1
        if 0<=x+i<N and 0<=y-i<N:
            if (x+i,y-i) not in d1:d1[(x+i,y-i)]=1
    return d1

def func(x,y,dic_check,count):
    global res,ch
    if y==N:
        x+=1
        y=0

    if x==N or len(dic_check)>=N*N:
        res=max(res,count)
        ch+=1
        return
    if (x,y) not in dic_check:
        tmp_check=updates(x,y)
        tmp_check.update(dic_check)
        func(x,y+1,tmp_check,count+1)

    func(x,y+1,dic_check,count)
dic={}
ch=0
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(N):
        if tmp[j]==0:
            dic[(i,j)]=1
    li.append(tmp)

func(0,0,dic,0)
print(res)
print(ch)