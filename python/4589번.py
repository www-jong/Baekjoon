print('Gnomes:')
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if [a,b,c]==sorted([a,b,c]) or [a,b,c]==sorted([a,b,c],reverse=True):
        print('Ordered')
    else:
        print('Unordered')
    