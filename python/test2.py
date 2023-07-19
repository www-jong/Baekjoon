N=6
print(bin(2**(N+2)))
to_bit=[2**i for i in range(N-1,-1,-1)]
def bit_masking(members,type):
    tmp=2**(N+1)-1
    for member in members:
        tmp-=to_bit[member]
    if type=='A':
        for i in range(N//2):
            tmp-=2**i
    else:
        for i in range(N//2,N):
            #pass
            tmp-=2**i
        tmp-=2**(N)
    return bin(tmp)[2:]
print(bit_masking([1,2],"A"))