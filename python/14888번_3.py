from itertools import permutations
arr=[]
INF=1000000000
maxv=-INF
minv=INF
n=int(input())
nums=list(map(int,input().split()))
sepas=list(map(int,input().split()))
sepa=['+']*sepas[0]+['-']*sepas[1]+['*']*sepas[2]+['/']*sepas[3]
sepalist=list(set(permutations(sepa, n-1)))
for s_list in sepalist:
    vv=nums[0]
    for i in range(n-1):
        comp='vv'+s_list[i]+str(nums[i+1])
        vv=int(eval(comp))
    if vv>maxv:maxv=vv
    if vv<minv:minv=vv
print(maxv)
print(minv)