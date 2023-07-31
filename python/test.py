

def func1(idx):
    if idx>=100:
        print('.',end='')
        return
    if idx%2==0:
        func1(idx+1)
    else:
        func1(idx+3)

func1(0)