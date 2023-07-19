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

res=[2**(N+2),10**17]
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

to_bit=[2**i for i in range(N-1,-1,-1)]
def bit_masking(members,type):
    tmp=2**(N+1)-1
    for member in members:
        tmp-=to_bit[member]
    if type=='A':
        for i in range(N//2):
            tmp-=2**i
    else:
        for i in range(N//2,N):
            #pass
            tmp-=2**i
        tmp-=2**(N)
    return bin(tmp)[2:]


def func(m):
    global res
    overlap_B={}
    sum_A=[]
    sum_B=[]
    for i in combinations(liA,m):
        print(i,res_A(i),int(bit_masking(i,"A"),2))
        sum_A.append([res_A(i),int(bit_masking(i,"A"),2)])
    for i in combinations(liB,N//2-m):
        tmp_sum_b=res_B(i)
        if str(m)+"_"+str(tmp_sum_b) not in overlap_B:
            overlap_B[str(m)+"_"+str(tmp_sum_b)]=[int(bit_masking(i,"B"),2)]
        else:
            overlap_B[str(m)+"_"+str(tmp_sum_b)].append(int(bit_masking(i,"B"),2))
        sum_B.append([tmp_sum_b,int(bit_masking(i,"B"),2)])
    sum_B.sort(key=lambda x:(x[0],x[1]))
    print(f'sum_A: {sum_A}')
    print(f'sum_B: {sum_B}')
    print(f'overlap : {overlap_B}')
    for i in range(len(sum_A)):
        start=0
        end=len(sum_B)
        while start<end:
            mid=(start+end)//2
            print(f'mid : {mid}')
            tmp_sum=sum_A[i][0]+sum_B[mid][0]
            tmp_lap=sum_B[mid][1]+sum_A[i][1]
            print(f'tum_sum: {tmp_sum}/{res[1]}, A :{sum_A[i][0]}/{bin(sum_A[i][1])[2:]}, B:{sum_B[mid][0]}/{bin(sum_B[mid][1])[2:]}, lap:{tmp_lap}:{res[0]}')
            if abs(tmp_sum)<res[1]:
                res[0]=min(overlap_B[str(m)+"_"+str(sum_B[mid][0])])+sum_A[i][1]
                print(f'{sum_B[mid][1]}+{sum_A[i][1]} =>{tmp_lap}')
                res[1]=abs(tmp_sum)
                #res=[sorted(overlap_B[sum_B[mid][0]])[0]+sum_A[i][1],tmp_sum]
                print(f'res:{res[1]} , {overlap_B[str(m)+"_"+str(sum_B[mid][0])]}')
                if tmp_sum==0:
                    break
                elif tmp_sum>0:
                    end=mid
                else:
                    start=mid+1
            elif abs(tmp_sum)==res[1]:
                if tmp_lap<res[0]:
                    print(f'!!{tmp_lap} , {res[0]}')
                    res[0]=tmp_lap
                end=mid
            elif tmp_sum>0:
                end=mid
            else:
                start=mid+1

                


for aa in range(N//2+1):
    func(aa)
if N!=1:
    for i in bin(res[0])[3:]:
        print(int(i)+1,end=" ")
else:
    print(2 if pointA[0]>pointB[0] else 1)

'''
6
120 1310 3124 1 1 1
1 1 1 1204 142 1245
> 2 2 2 1 1 1

6
1 1 1 23123 12421 52352353 
12312 4943 3412 1 1 1
> 1 1 1 2 2 2

2
1 1
2 2
>1 2

4
50 50 50 1
30 30 30 150
> 1 2 2 1

6
1 1 1 1 1 1
1 1 1 1 2 2
> 1 2 2 2 1 1

6
100 1 1 1 1 1
1 1 1 1 1 1
> 2 1 1 1 2 2

6 (41퍼)
100 1 100 1 100 1
100 1 100 1 100 1
> 1 1 1 2 2 2
'''