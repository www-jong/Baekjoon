S=input()
def get_weight(idx):
    t=0
    while idx<len(S):
        if S[idx]=="(":
            idx,g=get_weight(idx+1)
            t+=g
        elif S[idx]==")":
            if len(S)>idx+1:
                if S[idx+1].isnumeric():
                    return idx+1,t*int(S[idx+1])
                else:
                    return idx,t
            else:
                return idx,t
        elif S[idx] in "CHO":
            t+=weight[S[idx]]
        elif S[idx].isnumeric():
            t+=weight[S[idx-1]]*(int(S[idx])-1)
        idx+=1
    return idx,t
weight={'H':1,'C':12,'O':16}
stk=[]
idx=0
res=0
idx,r=get_weight(0)
print(r)