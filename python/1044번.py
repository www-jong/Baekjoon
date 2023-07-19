from itertools import combinations
N=int(input())
pointA=list(map(int,input().split()))
pointB=list(map(int,input().split()))
sum_pointB=sum(pointB)
liA=[i for i in range(N//2)]
liB=[i for i in range(N//2,N)]

res=[[],10**15]
rr=[]
def res_A(members):
    tmp=0
    for member in members:
        tmp+=pointA[member]
    return tmp

def res_B(members):

    tmp=sum_pointB
    for member in members:
        tmp-=pointB[member]
    return tmp

def func(m):
    member_A={}
    sum_A=[]
    sum_B=[]
    for i in combinations(liA,m):
        sum_A.append([res_A(i),i])
    for i in combinations(liB,N//2-m):
        sum_B.append([res_A(i),i])
    #print(member_A)
    sum_B.sort()
    
    for i in range(len(sum_A)):
        for j in range(len(sum_B)):
            one_team=sum_A[i][0]+sum_B[j][0]
            two_team=res_B(sum_A[i][1]+sum_B[j][1])
            #print(f'now team 1: {sum_A[i][1]+sum_B[j][1]}, gap={abs(one_team-two_team)}, {one_team} : {two_team}| {sum_A[i]} : {sum_B[j]}')
            if abs(one_team-two_team)<res[1]:
                res[1]=abs(one_team-two_team)
                tmp_li=[2 for i in range(N)]
                for k in sum_A[i][1]+sum_B[j][1]:
                    tmp_li[k]=1
                res[0]=tmp_li
            elif abs(one_team-two_team)==res[1]:
                pass
for aa in range(1,N//2+1):
    func(aa)
print(*res[0])