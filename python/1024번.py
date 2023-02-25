N,L=map(int,input().split())

for i in range(L,101):
    x=N-(i*(i+1)/2)
    if x%i==0:
        x=int(x//i)
        if (x+1)>=0:
            for j in range(1,i+1):
                print(x+j,end=' ')
            print()
            break
else:
    print(-1)

'''
N=(x+1)+(x+2)...(X+L)
=Lx+(1+2+3+4...L-1)
=Lx+(L-1)L/2
-> Lx=N-(L-1)L/2
즉, N-(L-1)L/2 를 L로 나누었을때 나머지가 0으로 나누어 떨어져야함
나누어 떨어진다면 x가 정수가 되기 때문에 정수개의 리스트가 나옴
이때, 처음 리스트의 시작인 x+1은 0보다 같거나 커야함


'''