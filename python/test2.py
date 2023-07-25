import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline


while True:
    li=list(map(int,input().split()))
    res=0
    if li[0]==0:break
    else:li.pop(0) 
    stk=[]
    min_check=[li[0],0]
    ch_idx=0
    for i in li:
        min_check=[min(min_check[0],i),min_check[1]+1]
        res=max(min_check[0]*min_check[1],res)
        idx=1
        if not stk:
            stk.append((i,ch_idx))
            ch_idx+=1
        else:
            if stk[-1][0]<i:
                stk.append((i,ch_idx))
                ch_idx+=1
            else:
                tmp_li=[]
                while stk[-1][0]>=i:
                    now_val,now_idx=stk.pop()
                    idx+=1
                    if not stk:
                        res=max(res,now_val*(ch_idx))
                        break
                    else:
                        res=max(res,now_val*(ch_idx-stk[-1][1]-1))
                res=max(res,i*idx)
                stk.append((i,ch_idx))
                ch_idx+=1
    print(stk,ch_idx)
    idx=1
    while stk:
        now_val,now_idx=stk.pop()
        if not stk:
            res=max(res,now_val*(ch_idx))
        else:
            res=max(res,now_val*(ch_idx-stk[-1][1]-1))
        idx+=1
    print(res)
