n=int(input())
tmp=''
s=[]
for i in range(n):
    t=' '+input()
    idx=t.index('<')
    idx2=t.index('>')
    s1=t[:idx]
    s2=t[idx+1:idx2]
    t=t[:idx]+t[idx+1:idx2]+t[idx2+1:]
    idx3=t.index('<')
    idx4=t.index('>')
    s3=t[idx2-1:idx3]
    s4=t[idx3+1:idx4]
    s5=t[idx4+1:]
    t=t[:idx3]+t[idx3+1:idx4]+t[idx4+1:]
    words2=t[idx+1:idx2]
    s.append(s1+s2+s3+s4+s5)
    tmp=s4+s3+s2+s5
    print(s1[1:]+s2+s3+s4+s5)
    print(input()[:-3]+tmp)
