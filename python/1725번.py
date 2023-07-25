import sys
input=sys.stdin.readline

li=[]
N=int(input())
for i in range(N):
    li.append(int(input()))
res=0
stk=[]
idx=0
for i in li:
    if not stk:
        stk.append((i,idx))
        idx+=1
    else:
        if stk[-1][0]<i:
            stk.append((i,idx))
            idx+=1
        else:
            tmp_li=[]
            while stk[-1][0]>=i:
                now_val,now_idx=stk.pop()
                if not stk:
                    res=max(res,now_val*(idx))
                    break
                else:
                    res=max(res,now_val*(idx-stk[-1][1]-1))
            stk.append((i,idx))
            idx+=1
while stk:
    now_val,now_idx=stk.pop()
    if not stk:
        res=max(res,now_val*(idx))
    else:
        res=max(res,now_val*(idx-stk[-1][1]-1))
print(res)
