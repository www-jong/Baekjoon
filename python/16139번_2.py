import sys
input=sys.stdin.readline
S="_"+input().rstrip()
li=[[0]*26]
for i in range(1,len(S)):
    li.append(li[i-1].copy())
    li[i][ord(S[i])-97]+=1
for i in range(int(input())):
    a,l,r=input().rstrip().split()
    print(li[1+int(r)][ord(a)-97]-li[int(l)][ord(a)-97])
# pypy와 sys.stdin.readline이 필수적