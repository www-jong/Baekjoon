while True:
    li=list(map(int,input().split()))
    A,B,C=sorted(li,reverse=True)
    if A==0 and B==0 and C==0:
        break
    if A>=B+C:
         print('Invalid')
    elif A==B==C:
        print('Equilateral')
    elif A==B or B==C or A==C:
        print('Isosceles')
    else:
        print('Scalene')