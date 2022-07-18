import sys
input=sys.stdin.readline
n=int(input())
dic={}
li=[]
for i in range(n):
    a,b=map(int,input().split())
    if a in dic:
        if dic[a]>b and a!=b:
            dic[a]=b
    else:
        dic[a]=b    
    if a==b:
        li.append((a,b))
for i in dic.keys():
    if i==dic[i]:
        continue
    li.append((i,dic[i]))
li.sort()
print(li)
'''
백트래킹이 안됨 시간초과
'''
