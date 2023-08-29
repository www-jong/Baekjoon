n=int(input())
li=[input()for i in range(n)]

s=int(input())
if s==1:
    for i in range(n):
        print(*li[i],sep='')
elif s==2:
    for i in range(n):
        print(*li[i][::-1],sep='')
elif s==3:
    for i in range(n):
        print(*li[n-1-i],sep='')