def fac(N):
    if N==1:
        return 1
    elif N==0:
        return 0
    return N*fac(N-1)
N=int(input())
print(fac(N))
