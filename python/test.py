R,I,P=range,input,print
for m in R(int(I())):
 n=[[1]];P(f'#{m+1}')
 for i in R(int(I())):
  n+=[[1,*[sum(n[-1][j:j+2])for j in R(i)],1]]
  P(*n[i])
