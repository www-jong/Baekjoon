N=int(input())
li=[]
min_x,min_y,max_x,max_y=10**5,10**5,0,0
for i in range(N):
    x,y=map(int,input().split())
    min_x,min_y,max_x,max_y=min(x,min_x),min(y,min_y),max(x,max_x),max(y,max_y)
print((max_x-min_x)*(max_y-min_y))