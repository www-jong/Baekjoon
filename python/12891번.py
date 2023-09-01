S,P=map(int,input().split())
code=input()
li=list(map(int,input().split()))
check={'A':li[0],'C':li[1],'G':li[2],'T':li[3]}
res=0
st,end=0,P-1
dic={'A':0,'C':0,'G':0,'T':0}
res=0
for i in code[st:end+1]:
    dic[i]+=1
while end<S-1:
    tmp=0
    for i in "ACGT":
        if dic[i]<check[i]:
            tmp=1
            break
    if not tmp:
        res+=1
    dic[code[st]]-=1
    st+=1
    end+=1
    dic[code[end]]+=1
tmp=0
for i in "ACGT":
    if dic[i]<check[i]:
        tmp=1
        break
if not tmp:
    res+=1
print(res)