N=list(bin(int(input()))[2:].zfill(32))
a=[]
for i in N:
    if i=='0':a.append('1')
    else:a.append('0')
a=list(bin(int('0b'+''.join(a),2)+1)[2:].zfill(32))
print(len([i for i in range(32) if N[i]!=a[i]]))