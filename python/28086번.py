S=input()
a,b,c=0,0,''
if "+" in S:
    a,b=S.split("+")
    c='+'
elif "*" in S:
    a,b=S.split("*")
    c='*'
elif "/" in S:
    a,b=S.split("/")
    c='//'
else:

    i=1
    while True:
        if S[i]=='-':
            a,b=S[:i],S[i+1:]
            break
        i+=1
    c='-'

try:
    g=eval(f'{str(int(a,8))}{c}{str(int(b,8))}')
    print(oct(g)[2:] if oct(g)[0]!='-' else '-'+oct(g)[3:])
except:
    print('invalid')
