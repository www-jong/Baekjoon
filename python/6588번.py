from sys import stdin
arr=[1 for _ in range(1000001)]
so=[]
dic={}
for i in range(2,1001):
    if arr[i]:
        for j in range(i+i,1000001,i):
            arr[j]=0

for i in range(3,1000001):
    if arr[i]==1:
        so.append(i)
        dic[i]=1

while True:
    c=int(stdin.readline())
    b=0
    idx=0
    if c==0:
    	break
    for i in range(len(so)):
        if c-so[i] in dic and so[i] in dic:
            print(f'{c} = {so[i]} + {c-so[i]}')
            b=1
            break
    if b==0:
        print("Goldbach's conjecture is wrong.")