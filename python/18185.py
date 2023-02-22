N=int(input())
res=0
def buythree(idx):
    global res
    k=min(li[idx:idx+3])
    for i in range(idx,idx+3):
        li[i]-=k
    res+=7*k

def buytwo(idx,type=0):
    global res
    if type==1:
        k=min(li[idx],li[idx+1]-li[idx+2])
    else:
        k=min(li[idx:idx+2])
    for i in range(idx,idx+2):
        li[i]-=k
    res+=5*k

def buyone(idx):
    global res
    k=li[idx]
    li[idx]-=k
    res+=3*k


li=[0]+list(map(int,input().split()))+[0,0]

for i in range(1,N+1):
    if li[i]!=0:
        if li[i+1]>li[i+2]:
            buytwo(i,1)
            buythree(i)
        else:
            buythree(i)
            buytwo(i)
        buyone(i)
print(res)
'''
102
201
100
010

'''