N=int(input())
M=int(input())
S=input()
n_s='I'+'OI'*N
res=0
count=0
plag=0
for i in S:
    if not plag:
        if i=="I":
            plag=1
            count+=1
        else:
            count=0
    else:
        if i=="O":
            plag=0
            count+=1
        else:
            plag=1
            count=1
    if count==1+2*N:
        res+=1
        count-=2
print(res)


