N,A,B=map(int,input().split())
if A<N:
    print('Bus')
elif A==N:
    if N==B:
        print('Anything')
    else:
        print('Bus')
else:
    if A==B:
        print('Anything')
    elif A<B:
        print('Bus')
    else:
        print('Subway')