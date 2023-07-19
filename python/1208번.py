from itertools import combinations
N,S=map(int,input().split())
li=list(map(int,input().split()))

liA=li[:N//2]
liB=li[N//2:]

sunA=[]
sunB=[]
dic={}
for i in range(1,len(liA)+1):
    for j in combinations(liA,i):
        sunA.append(sum(j))

for i in range(1,len(liB)+1):
    for j in combinations(liB,i):
        tmp=sum(j)
        if tmp not in dic:
            dic[tmp]=1
        else:
            dic[tmp]+=1
        sunB.append(tmp)

sunB.sort()
res=0
for i in sunA:
    if i==S:
        res+=1
for i in sunB:
    if i==S:
        res+=1

for ele_A in sunA:

    st=0
    end=len(sunB)
    while st<end:
        mid=(st+end)//2
        if ele_A+sunB[mid]>S:
            end=mid
        elif ele_A+sunB[mid]==S:
            res+=dic[sunB[mid]]
            break
        else:
            st=mid+1

print(res)
'''
def func(start,end):
    global res
    mid=(start+end)//2
    if A+sunB[mid]==S:
        res+=1
    elif A+sunB[mid]>S:
        func(start,mid)
    else:
        func(mid+1,end)

for A in sunA:

    start=0
    end=len(sunB)
    func(start,end)

print(res)
print(sunA)
print(sunB)

1 : 5
2 : 10
3 : 10
4 : 5
5 : 1
'''