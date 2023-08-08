N=int(input())
li=list(map(int,input().split()))
res="Nice"
stk,idx=[],1
for i in li:
    while stk and stk[-1]==idx:
        stk.pop()
        idx+=1
    if i==idx:
        idx+=1
        continue
    if stk:
        if i>stk[-1]:
            res="Sad"
            break
        else:
            stk.append(i)
    else:
        stk.append(i)

print(res)