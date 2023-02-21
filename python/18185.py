N=int(input())
res=0
def buythree(idx):


li=[0]+list(map(int,input().split()))+[0,0]

for i in range(1,N+1):
    if li[i]>li[i+1]:
        
