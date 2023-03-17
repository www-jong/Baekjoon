S=input()
ch_0=0
ch_1=0
if S[0]=='0':
    ch_1+=1
else:
    ch_0=1

tmp=S[0]
for i in range(len(S)):
    if S[i]!=tmp:
        if S[i]=='1':
            ch_0+=1
        else:
            ch_1+=1
    tmp=S[i]
print(min(ch_0,ch_1))