from sys import stdin
arr=[1 for _ in range(1000001)]
for i in range(2,1001):
    if arr[i]:
        for j in range(i+i,1000001,i):
            arr[j]=0

while True:
    c=int(stdin.readline())
    b=0
    if c==0:break

    for i in range(3,len(arr)):
        if arr[i] and arr[c-i]:
            print(f'{c} = {i} + {c-i}')
            b=1
            break

    if b==0:
        print("Goldbach's conjecture is wrong.")