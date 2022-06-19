dic={}
for i in range(1,20):
    dic[(i,i**3)]=(i,i*2,i**2)
for (a,b),(c,d,e) in dic.items():
    print('%d %d %d %d %d'%(a,b,c,d,e))