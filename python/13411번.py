import sys
input=sys.stdin.readline
r=[]
for i in range(int(input())):
    x,y,v=map(int,input().split())
    r.append([((x**2+y**2)**(0.5))/v,i+1])
r.sort(key=lambda x:(x[0],x[1]))
for i in r:
    print(i[1])