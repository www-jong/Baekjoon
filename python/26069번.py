N=int(input())
dic={}
for i in range(N):
    A,B=map(str,input().split())
    if A=='ChongChong' or B=='ChongChong' or A in dic or B in dic:
        if A not in dic:
            dic[A]=1
        if B not in dic:
            dic[B]=1
print(len(dic))
