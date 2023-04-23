R,C=map(int,input().split())
li=[[0]*(C+1)]
for i in range(R):
    li.append([0]+list(map(int,input().split())))
res=''
if R%2==0:
    