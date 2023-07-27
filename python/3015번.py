import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
stk=[]
res=0
dic={}
max_hi_chk=-1
def adds(val):
    global dic
    ress=0
    if val in dic and dic[val]!=0:
        ress=int((dic[val]+1)*(dic[val]/2))
        del dic[val]
    if len(stk)!=0 and stk[0][0]==val:
        ress-=1
    return ress

for i in range(N):
    while stk:
        h,w=stk.pop()
        if li[i]<=h: # 더 작은키가 들어올때,
            res+=1
            stk.append((h,w))
            break
        else: # 더 큰 키가 들어올 때,
            res+=adds(h)   
            res+=1
    stk.append((li[i],i))
    if li[i] not in dic:
         dic[li[i]]=0
    else:
         dic[li[i]]+=1
    print(f'{i} == {stk},  res={res}, dic:{dic}')

for x,i in stk:
    if x in dic:
        if dic[x]!=0:
            res+=int((dic[x]+1)*(dic[x]/2))
            del dic[x]
print(dic)
print(stk)
print(res)
# 중복될때,   중복되는키 앞에 더 큰키가 있을때, 중복되는키가 제일 클때