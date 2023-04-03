N=int(input())
if N%6!=0:
    for i in range(1,N+1):
        print(i,end=' ')
        if i%6==0:
            print('Go!',end=' ')
    print('Go!',end=' ')
else:
    for i in range(1,N+1):
        print(i,end=' ')
        if i%6==0:
            print('Go!',end=' ')