N=int(input())
li=sorted(list(map(int,input().split())))
st=li[0]
res=[10**8,-1]
ab=[0,0,0]
now=0
dic={}
for i in li:
    if st>i:
        ab[0]+=1
    elif st==i:
        ab[1]+=1
    else:
        ab[2]+=1
    now+=abs(i-st)
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(ab,now)
print(li)
res=[now,st]
st+=1
while st<=li[-1]:
    tmp=0
    tmp=now+ab[0]+ab[1]
    print(f"{st} {(0 if st not in dic else dic[st])}")
    tmp-=ab[2]
    print(f'{tmp} {now} {st}')
    if res[0]>tmp:
        res=[tmp,st]
    ab[0]+=ab[1]
    ab[1]=(0 if st not in dic else dic[st])
    ab[2]=ab[2]-ab[1]
    st+=1
    now=tmp
print(res)
