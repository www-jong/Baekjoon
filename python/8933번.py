def rec(now):
    s=''
    for k,v in now.items():
        s+=k+str(v)
    return s
T=int(input())
for i in range(T):
    a,b=input().split()
    a=int(a)
    dic={}
    st,end=0,a
    now={"A":0,"C":0,"G":0,"T":0}
    for i in range(end):
        now[b[i]]+=1
    dic[rec(now)]=1
    while end<len(b):
        now[b[end]]+=1
        now[b[st]]-=1
        print(st,end,now)
        st+=1
        if rec(now) not in dic:
            dic[rec(now)]=1
        else:
            dic[rec(now)]+=1
        end+=1

    print(max([i for i in dic.values()]))