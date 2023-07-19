N=int(input())

def bitcount(n):
    if n==0:
        return 0
    return n%2+bitcount(n//2)

def finds(M):
    idx=0
    while True:
        if M<(2**idx)*2:
            break
        idx+=1
    return idx
for i in range(N):
    M=int(input())
    if M==1:
        print(0,0)
        continue
    m=bin(M)[-1:1:-1]

    if m.count('1')==2:
        x=m.find('1')
        y=m.find('1',x+1)
        print(x,y)
    elif m.count('1')==1:
        x=m.find('1')
        print(x-1,x-1)
    else:
        
        m=bin(M)[2::]

        y=len(bin(M))-3-m.find('1')
        x=len(bin(M))-3-m.find('1',m.find('1')+1)
        #print(x,y)
        res=[10**19,x,y]
        for i in range(y+1):
            for j in range(y,y+2):
                if res[0]>abs(M-2**i-2**j):
                    res=[abs(M-2**i-2**j),i,j]
        if res[0]>abs(M-2**0-2**(y+1)):
                res=[abs(M-2**0-2**(y+1)),0,y+1]
        print(res[1],res[2])
