while True:
    a,b=map(float,input().split())
    if a==0 and b==0:
        print('AXIS')
        break
    if a>0 and b>0:
        print('Q1')
    elif a>0 and b<0:
        print('Q4')
    elif a<0 and b<0:
        print('Q3')
    elif a<0 and b>0:
        print('Q2')
    else:
        print('AXIS')