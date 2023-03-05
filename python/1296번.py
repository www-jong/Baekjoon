def res_grade(S):
    global yun
    dic={'L':0,'O':0,'V':0,'E':0}
    for i in yun+S:
        if i in dic:
            dic[i]+=1

    return ((dic['L']+dic['O'])*(dic['L']+dic['V'])*(dic['L']+dic['E'])*(dic['O']+dic['V'])*(dic['O']+dic['E'])*(dic['V']+dic['E']))%100
yun=input()
res=[-1,'']

N=int(input())
for i in range(N):
    S=input()
    S_val=res_grade(S)
    if res[0]<S_val:
        res=[S_val,S]
    elif res[0]==S_val:
        if sorted([S,res[1]])[0]==S:
            res=[S_val,S]
print(res[1])