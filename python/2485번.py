import sys
input=sys.stdin.readline
N=int(input())
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
li=[]
res=0
for i in range(N):
    li.append(int(input()))
li.sort()
gcds=[]
for i in range(1,N):
    gcds.append(li[i]-li[i-1])
gcd_val=li[1]-li[0]
for i in gcds:
    gcd_val=gcd(gcd_val,i)
print((li[-1]-li[0])//gcd_val-(N-1))
print(gcd_val)


'''
1 3 6 10 15
'''