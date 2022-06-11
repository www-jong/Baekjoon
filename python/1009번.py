import sys
a=0
for i in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    ans=pow(a,b,10)

    sys.stdout.writelines(str(10 if ans==0 else ans)+"\n")
    
