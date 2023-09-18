import sys
sys.setrecursionlimit(10**8)
num=int(input())
L=int(input())
R=int(input())
N=int(input())
trans=[0,'132','211','232']
def gets(tmp,dep):
    if dep==N:
        return tmp
    tmp_s=[0,0,0]
    tmp_s[0]+=tmp[0]+tmp[1]*2
    tmp_s[1]+=tmp[0]+tmp[1]+tmp[2]*2
    tmp_s[2]+=tmp[0]+tmp[2]
    return gets(tmp_s,dep+1)
def func(idx,n,dep):
    global res
    if dep==N:
        if L<=idx<=R:
            res[n]+=1
        return
    val=trans[n]
    l,m,r,rr=idx,idx+3**(N-dep-1),idx+2*(3**(N-dep-1)),idx+3*(3**(N-dep-1))
    if L<=l<=R or L<=m-1<=R or (l<=L and R<=m-1):
        if L<=l and m-1<=R:
            tmp=[0,0,0]
            tmp[int(val[0])-1]+=1
            tmp_v=gets(tmp,dep+1)
            for i in range(3):
                res[i+1]+=tmp_v[i]
        else:
            func(idx,int(val[0]),dep+1)
    if L<=m<=R or L<=r-1<=R or (m<=L and R<=r-1):
        if L<=m and r-1<=R:
            tmp=[0,0,0]
            tmp[int(val[1])-1]+=1
            tmp_v=gets(tmp,dep+1)
            for i in range(3):
                res[i+1]+=tmp_v[i]
        else:
            func(idx+3**(N-dep-1),int(val[1]),dep+1)
    if L<=r<=R or L<=rr-1<=R or (r<=L and R<=rr-1):
        if L<=r and rr-1<=R:
            tmp=[0,0,0]
            tmp[int(val[2])-1]+=1
            tmp_v=gets(tmp,dep+1)
            for i in range(3):
                res[i+1]+=tmp_v[i]
        else:
            func(idx+2*(3**(N-dep-1)),int(val[2]),dep+1)


res=[0,0,0,0]
func(0,num,0)
#if N==0:
#    res[num]=1
print(*res[1:])
