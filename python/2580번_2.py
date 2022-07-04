maps=[[0]*(10)]
emp=[]
for i in range(9):
    tmp=list(map(int,input().split()))
    for j in range(9):
        if tmp[j]==0:
            emp.append((i+1,j+1))
    maps.append([0]+tmp)
print('---------')
def checks(a,b,m=0):
    re=set([1,2,3,4,5,6,7,8,9])
    tmp1,tmp2,tmp3=[],[],[]
    check=0
    if maps[a][b]==0 and m==0:
        for i in range(1,10):
            if b!=i:
                tmp1.append(maps[a][i])
            if a!=i:
                tmp2.append(maps[i][b])
            if (((a-1)//3)*3+1+(i-1)//3,((b-1)//3)*3+1+(i-1)%3)!=(a,b):
                tmp3.append(maps[((a-1)//3)*3+1+(i-1)//3][((b-1)//3)*3+1+(i-1)%3])
        if len(re-set(tmp1))==1:
            maps[a][b]=list(re-set(tmp1))[0]
            check=1
        elif len(re-set(tmp2))==1:
            maps[a][b]=list(re-set(tmp2))[0]
            check=1
        elif len(re-set(tmp3))==1:
            maps[a][b]=list(re-set(tmp3))[0]
            check=1
        return check
    elif m==1:
        ans=[]
        for i in range(1,10):
            if b!=i:
                tmp1.append(maps[a][i])
            if a!=i:
                tmp2.append(maps[i][b])
            if (((a-1)//3)*3+1+(i-1)//3,((b-1)//3)*3+1+(i-1)%3)!=(a,b):
                tmp3.append(maps[((a-1)//3)*3+1+(i-1)//3][((b-1)//3)*3+1+(i-1)%3])
        ans=list(re-set(tmp1)-set(tmp2)-set(tmp3))
        return ans

def func(idx):
    if idx==(len(emp)):
        for i in range(1,10):
            print(*maps[i][1:10])
            if i in [3,6,9]:
                print('----')
        exit(0)
    aval=checks(emp[idx][0],emp[idx][1],1)
    for i in aval:
        maps[emp[idx][0]][emp[idx][1]]=i
        func(idx+1)
        maps[emp[idx][0]][emp[idx][1]]=0
for _ in range(3):
    emp2=[]
    for i in range(len(emp)):
        check=checks(emp[i][0],emp[i][1])
        if check==0:
            emp2.append(emp[i])
    emp=emp2
if len(emp)==0:
    for i in range(1,10):
        print(*maps[i][1:10])
else:
    func(0)