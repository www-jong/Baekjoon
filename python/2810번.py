N=int(input())
S=list(input())
res=0
ch=0
tmp='.'
idx=0

while idx<N:
    if S[idx]=='S':
        if tmp[-1]!="*":
            tmp+="*"+S[idx]
            res+=1
        elif tmp[-1]=="*":
            tmp+=S[idx]
        idx+=1
    elif S[idx]=="L":
        if tmp[-1]!="*":
            tmp+="*"+"LL"+"*"
            idx+=2
            res+=2
        elif tmp[-1]=="*":
            tmp+="LL"+"*"
            idx+=2
            res+=1
    else:
        idx+=1
print(res)