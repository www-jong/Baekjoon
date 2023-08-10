def D(n):
    n=int(n)*2%10000
    if n<1000:
        n='0'+str(n)
    else:
        n=str(n)
    return n
def S(n):
    return int(n)-1 if n!='0000' else '9999'
def L(n):
    return int(str(n)[1:]+str(n)[0])
def R(n):
    return int(str(n)[-1]+str(n)[:-1])