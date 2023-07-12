import copy
N=int(input())
s=input()

num=[['',''] for _ in range(N//2+1)]
formula=['']*(N//2)
for i in range(0,N//2):
    num[i][0]=int(s[i*2])
    num[i][1]=int(s[i*2+2])
    num[i+1][0]=int(s[i*2+2])
    formula[i]=s[i*2+1]

max_val=-2**33

def calc(snum,sformula,x):
    if len(sformula)==0:
        return snum,sformula,0
    tmp=eval(str(snum[x][0])+sformula[x]+str(snum[x][1]))
    del snum[x]
    del sformula[x]
    snum[x][0]=tmp
    if x!=0:
        snum[x-1][1]=tmp

    return snum,sformula,tmp
tmp=0

def func(idx,li):
    global max_val
    tnum=copy.deepcopy(num)
    tformula=copy.deepcopy(formula)
    if idx>=N//2:
        ttmp2=-10**10
        li.sort()
        for i in range(len(li)):
            tnum,tformula,_=calc(tnum,tformula,li[i]-i)
        for i in range(len(tformula)):
            tnum,tformula,ttmp2=calc(tnum,tformula,0)
        max_val=max(max_val,ttmp2)
        return
    
    for l in range(idx,N//2):
        li.append(l)
        func(l+2,li)
        li.pop()
        func(l+1,li)

func(0,[])
print(max_val if N!=1 else int(s[0]))