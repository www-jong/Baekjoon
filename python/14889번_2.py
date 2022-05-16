from itertools import combinations
import sys
n=int(sys.stdin.readline())
allmember=[i for i in range(1,n+1)]
pick=[]
temp=[]

for i in combinations(allmember,n//2):
    pick.append(list(i))

li=[[0]*(n+1)]
for i in range(n):
    li.append([0]+list(map(int,sys.stdin.readline().split())))
newli=[[0]]
def getpower(power,memberlist):
    for i,j in memberlist:
        power+=li[i][j]+li[j][i]
    return power

powergap=1000000
for bluemember in pick:
    gap=0
    blueteam=[]
    redteam=[]
    bpower=0
    rpower=0
    for i in combinations(bluemember,2):
        blueteam.append(list(i))
    redmember=list(set(allmember)-set(bluemember))
    for i in combinations(redmember,2):
        redteam.append(list(i))
    bpower=getpower(bpower,blueteam)
    rpower=getpower(rpower,redteam)
    gap=abs(bpower-rpower)
    if gap<powergap:
        powergap=gap
print(powergap)