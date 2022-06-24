import math
n=int(input())
rings=list(map(int,input().split()))
for i in range(1,len(rings)):
    gcd=math.gcd(rings[0],rings[i])
    print("%d/%d"%(rings[0]//gcd,rings[i]//gcd))