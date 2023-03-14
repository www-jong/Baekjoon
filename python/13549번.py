N,K=map(int,input().split())
dic={}
tmp_K=K
idx=1
while tmp_K<=100000:
    tmp_K=tmp_K*(2**idx)
    dic[tmp_K]=1
    idx+=1
idx=1
while tmp_K>=2:
    tmp_K=tmp_K*(0.5**idx)
    dic[tmp_K]=1
    idx+=1
li=[0]*(100001)
print(dic)
