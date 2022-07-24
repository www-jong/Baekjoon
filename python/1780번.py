import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
n=int(input())
maps=[[0]*(n+1)]

for i in range(n):
    maps.append([0]+list(map(int,input().split())))

mi,ze,on=0,0,0

def func(st,en):
    global mi,ze,on
    tmp1,tmp2=0,0
    half=(en[0]-st[0]+1)//3
    if st==en:
        if maps[en[0]][en[1]]==1:
            on+=1
        elif maps[en[0]][en[1]]==0:
            ze+=1
        else:
            mi+=1
    else:
        for i in range(st[0],en[0]+1):
            for j in range(st[1],en[1]+1):
                if maps[i][j]==1:
                    tmp1+=1
                elif maps[i][j]==-1:
                    tmp2+=1
        if tmp1==((half*3)**2):
            on+=1
        elif tmp1==0 and tmp2==0:
            ze+=1
        elif tmp2==((half*3)**2):
            mi+=1
        else:
            for i in range(st[0],en[0]+1,half):
                for j in range(st[1],en[1]+1,half):
                    func((i,j),(i+half-1,j+half-1))

func((1,1),(n,n))
print("%d\n%d\n%d"%(mi,ze,on))


'''
0,0 9,9
->
'''