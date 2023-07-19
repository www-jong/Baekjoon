from itertools import combinations
N=int(input())
pointA=list(map(int,input().split()))
pointB=list(map(int,input().split()))

liA=[i for i in range(N//2)]
liB=[i for i in range(N//2,N)]
sum_pointAA=sum([pointA[i] for i in liA])
sum_pointAB=sum([pointB[i] for i in liA])

sum_pointBA=sum([pointA[i] for i in liB])
sum_pointBB=sum([pointB[i] for i in liB])

res=[[],10**15]
rr=[]
def res_A(members):
    tmp=sum_pointAB
    for member in members:
        tmp-=pointA[member]+pointB[member]
    return tmp

def res_B(members):

    tmp=sum_pointBB
    for member in members:
        tmp-=pointA[member]+pointB[member]
    return tmp

def func(m):
    global res
    overlap_B={}
    sum_A=[]
    sum_B=[]
    for i in combinations(liA,m):
        sum_A.append([res_A(i),i])
    for i in combinations(liB,N//2-m):
        tmp_sum_b=res_B(i)
        if tmp_sum_b not in overlap_B:
            overlap_B[tmp_sum_b]=[i]
        else:
            overlap_B[tmp_sum_b].append(i)
        sum_B.append([tmp_sum_b,i])
    sum_B.sort(key=lambda x:x[0])
    print(f'sum_A: {sum_A}')
    print(f'sum_B: {sum_B}')
    print(f'overlap : {overlap_B}')
    for i in range(len(sum_A)):
        start=0
        end=len(sum_B)
        while start<end:
            mid=(start+end)//2
            tmp_sum=sum_A[i][0]+sum_B[mid][0]
            print(f'tum_sum: {tmp_sum}, A :{sum_A[i][0]}, B:{sum_B[mid][0]}')
            if abs(tmp_sum)<res[1]:
                res=[sorted(overlap_B[sum_B[mid][0]])[0]+sum_A[i][1],tmp_sum]
                print(f'res:{res[1]} , {overlap_B[sum_B[mid][0]]}')
                if tmp_sum==0:
                    break
                elif tmp_sum>0:
                    end=mid
                else:
                    start=mid+1
            elif tmp_sum>0:
                end=mid
            else:
                start=mid+1


for aa in range(1,N//2+1):
    func(aa)
res_li=[2 for _ in range(N)]
for i in res[0]:
    res_li[i]=1
print(*res_li)