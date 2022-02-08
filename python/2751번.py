import sys
a=[]
for i in range(int(input())):
    a+=[int(sys.stdin.readline())]
def mer(a):
    if len(a)<2:
        return a
    m=len(a)//2
    fir=mer(a[:m])
    sec=mer(a[m:])
    
    r_a=[]
    num_i=0
    num_j=0
    while num_i<len(fir) and num_j<len(sec):
        if fir[num_i]<sec[num_j]:
            r_a+=[fir[num_i]]
            num_i+=1
        else:
            r_a+=[sec[num_j]]
            num_j+=1
    r_a+=fir[num_i:]
    r_a+=sec[num_j:]
    return r_a
a=mer(a)
for i in range(len(a)):
    print(a[i])
