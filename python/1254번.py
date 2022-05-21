s=input()
count=0
best=0
ans=0
exits=0
for i in range(len(s)//2-1,len(s)): 
    best=1+len(s)*2
    count=0
    ans=0
    if i==len(s)//2-1 and len(s)%2==0:
        for j in range(i+1):
            print('1_i :%d, j :%d'%(i,j))
            if s[i-j]!=s[i+j+1]:
                ans=1
                break
        if ans==0:
            best=i*2+2
            exits=1
            break
    elif i!=len(s)//2-1:
        for j in range(i+1 if i< len(s)-i else len(s)-i):
            print('2_i :%d, j :%d'%(i,j))
            if s[i-j]!=s[i+j]:
                ans=1
                break
        if ans==1:
            if len(s)-i<i+1:
                for j in range(i+1 if i< len(s)-i else len(s)-i):
                    print('3_i :%d, j :%d'%(i,j))
                    if s[i-j+1]!=s[i+j]:
                        ans=2
                        break
                if ans==1:
                    best=i*2+2
                    exits=1
                    break
        if ans==0:
            best=1+i*2
            break
if len(s)==1:
    print('1')
else:
    print(best-1 if len(s)%2==0 and exit==0 else best)
