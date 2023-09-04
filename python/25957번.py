import sys
input=sys.stdin.readline
N=int(input())
dic={}
def gets(word):
    tmp={}
    for j in sorted(word[1:len(word)-1]):
        if j not in tmp:
            tmp[j]=1
        else:
            tmp[j]+=1
    return word[0]+word[-1],tmp

for i in range(N):
    s=input().rstrip()
    if len(s)<=3:
        continue
    else:
        tmp={}
        for j in sorted(s[1:len(s)-1]):
            if j not in tmp:
                tmp[j]=1
            else:
                tmp[j]+=1
        t=''
        for k,v in tmp.items():
            t+=str(k)+str(v)
        if s[0]+s[-1]+str(len(s)) not in dic:
            dic[s[0]+s[-1]+str(len(s))]={t:s}
        else:
            dic[s[0]+s[-1]+str(len(s))][t]=s
N=int(input())
S=input().rstrip().split()
for i in range(len(S)):
    if len(S[i])<=3:
        continue
    k,v=gets(''.join(S[i]))
    t=''
    for b,d in v.items():
        t+=str(b)+str(d)
    for k,v in dic[k+str(len(S[i]))].items():
        if t==k:
            S[i]=v
            break
print(*S)