N=int(input())
li=[[],[]]
for i in range(N):
    a,b=map(int,input().split())
    li[0].append(a)
    li[1].append(b)
print((max(li[0])+max(li[1])-min(li[1])-min(li[0]))*2)