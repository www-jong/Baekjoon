def f(now):
    global res
    if "" not in now and " " not in now and now:
        print(''.join(now)+" ",end='')
S=input()
res=[]
idx=0
token=[]
now=[]
while idx<len(S):
    if S[idx] not in "<>()||&& ":

        now.append(S[idx])
    else:
        f(now)
        now=[]
        if S[idx] in "&|":
            now.append(S[idx])
            now.append(S[idx])
            idx+=1
            f(now)
        else:
            f([S[idx]])
        now=[]
    idx+=1
f(now)
