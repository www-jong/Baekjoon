N=int(input())
A,B=map(int,input().split())
print(N if B+A//2 >N else B+A//2)