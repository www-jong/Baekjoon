import sys
for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    c=a**(b%4 if b%4!=0 else 4)%10
    print(c if c!=0 else 10)




'''
2 4 8 6 2
3 9 7 1 3
4 6 4
5 5
6 6
7 9 3 1 7
8 4 2 6 8
9 1 9

'''