for i in range(int(input())):
    N,M=map(int,input().split())
    print(11*M + 4 if N >= 12 and M >= 4 else -1)