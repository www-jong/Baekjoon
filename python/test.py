st=(1,1)
en=(9,9)
half=(en[0]-st[0]+1)//3
for i in range(st[0],en[0]+1,half):
  for j in range(st[1],en[1]+1,half):
    print("%d:%d %d:%d"%(i,j,i+half-1,j+half-1))

'''
1,1 9,9
->
1,1 3,3
1,4 3,6
1,7 3,9
4,1 6,3
4,4 6,6
4,7 6,9

'''