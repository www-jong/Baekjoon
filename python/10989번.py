import sys
n=int(input())
arr=[0]*10001
s=""
d="\n"
for i in range(n):
    arr[int(sys.stdin.readline())]+=1
for i in range(1,10001):
    if arr[i]!=0:
        for j in range(arr[i]):
             sys.stdout.write(str(i)+"\n")


#        s+=(str(i)+"\n")*arr[i]
#print(s)