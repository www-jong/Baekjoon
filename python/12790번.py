for i in range(int(input())):
    a,b,c,d,A,B,C,D=map(int,input().split())
    print((max(A+a,1)+5*(max(B+b,1))+2*(max(C+c,0))+2*(D+d)))
