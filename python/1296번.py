def res_grade(S):
    dic={'L':0,'O':0,'V':0,'E':0}
    for i in S:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return ((dic['L']+dic['O'])*(dic['L']+dic['V'])*(dic['L']+dic['E'])*(dic['O']+dic['V']*(dic['V']+dic['E'])))%100
yun=input()
res=[res_grade(yun),yun]

N=int(input())
for i in range(N):
    S=input()
    print(res_grade(S))
    if res[0]<res_grade(S):
        res=[res_grade(S),S]
print(res[1])