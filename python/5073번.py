while True:
    li=list(map(int,input().split()))
    A,B,C=sorted(li,reverse=True)
    if A==0 and B==0 and C==0:
        break
    if A==B==C:
        print('Equilateral')
    elif A==B or B==C or A==C:
        print('Isosceles')
    elif A!=B and B!=C and A!=C:
        if B+C<=A:
            print('Invalid')
        else:
            print('Scalene')
    else:
        print('Invalid')
