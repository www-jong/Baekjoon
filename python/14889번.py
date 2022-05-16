n=int(input())
allmember=[i for i in range(1,n+1)]
pick=[]
temp=[]
def func():
    global pick
    if len(temp)==n//2:
        pick.append(temp[:])
        return
    for i in range(1,n+1):
        if i in temp:
            continue
        if len(temp)!=0 and temp[-1]>i:
            continue
        temp.append(i)
        func()
        temp.pop()

def comb(pick1,combs):
    if len(temp)==2:
        combs.append(temp[:])
        return
    for j in range(len(pick1)):
        if pick1[j] in temp:
            continue
        if len(temp)!=0 and temp[-1]>pick1[j]:
            continue
        temp.append(pick1[j])
        comb(pick1,combs)
        temp.pop()

def getpower(power,memberlist):
    for i,j in memberlist:
        power+=li[i][j]+li[j][i]
    return power

func()
li=[[0]*(n+1)]
for i in range(n):
    li.append([0]+list(map(int,input().split())))

powergap=1000000
for bluemember in pick:
    gap=0
    blueteam=[]
    redteam=[]
    bpower=0
    rpower=0
    comb(bluemember,blueteam)
    redmember=list(set(allmember)-set(bluemember))
    comb(redmember,redteam)
    power=0
    bpower=getpower(bpower,blueteam)
    rpower=getpower(rpower,redteam)
    gap=abs(bpower-rpower)
    if gap<powergap:
        powergap=gap
print(powergap)