N,M=map(int,input().split())
li=[[0]]
homes=[]
chics=[]
all_selected_chics=[]
for i in range(1,N+1):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,N+1):
        if tmp[j]==1:
            homes.append([i,j])
        elif tmp[j]==2:
            chics.append([i,j])
    li.append(tmp)
len_chics=len(chics)

def choices(M,selected_chics,idx):
    global all_selected_chics
    if len(selected_chics)==M:
        all_selected_chics.append(selected_chics.copy())
        return
    
    for i in range(idx,len_chics):
        selected_chics.append(chics[i])
        choices(M,selected_chics,i+1)
        selected_chics.pop()
choices(M,[],0)
res=10**9
for choice_chics in all_selected_chics:

    tmp=0
    for x,y in homes:
        tmp_len=10**9
        for dx,dy in choice_chics:
            tmp_len=min(tmp_len,abs(x-dx)+abs(y-dy))
        tmp+=tmp_len
    res=min(res,tmp)
print(res)