N=int(input())
li=[]

def func(x,idx):
    global li
    if x!='':
        li.append(int(x))

    for i in range(idx+1,10):
        func(str(i)+str(x),i)

if N>1022:
    print(-1)
else:
    func('',-1)
    li.sort()
    print(li[N-1])