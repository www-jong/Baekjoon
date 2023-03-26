N=int(input())
res=[0,1,0]
while res[0]<N:
    res[0]+=res[1]+2
    res[1]+=2
    res[2]+=1
print(res[2])
'''
2000

'''