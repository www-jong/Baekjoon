p=list(map(int,input().split()))
x,y,r=map(int,input().split())
ch=0
for i in range(4):
    if p[i]==x:
        print(i+1)
        ch=1
        break
if ch==0:print(0)