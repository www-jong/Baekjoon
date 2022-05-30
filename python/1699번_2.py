'''
1=(1)             1
2=(1)*2           2
3=(1)*3           3
4=(2)             1
5=(2)+(1)         2
6=(2)+(1)*2       3
7=(2)+(1)*3       4
8=(2)*2           2
9=(3)             1
10=(3)+(1)        2
11=(3)+(1)*2      3
12=(2)*3          3
13=(3)+(2)        2
14=(3)+(2)+(1)    3
15=(3)+(2)+(1)*2  4
16=(4)            1
17=(4)+(1)        2
18=(3)*2          2
19=()
일반적으로 dp(n)=min(dp(n)+1,dp(e)*k,dp(s))  
이때, e는 dp(e)가 0이고 n%e==0인 어느 자연수
      s는 s**2=n를 만족하는 자연수

100000**(1/2)=316.227

특이점 : 13인경우, 4와 9로 이루어져 2를 가짐
'''
n=int(input())
dp=[0,1,2,3]
li=[]
for i in range(2,315):
    li.append(i**2)
li2=set()
li3=set()
for i in range(len(li)):
    for j in range(i+1,len(li)):
        li2.add(li[i]+li[j])
        for l in range(j+1,len(li)):
            li3.add(li[i]+li[j]+li[l])
for i in range(4,n+1):
    if i**(1/2)%1==0:
        dp.append(1)
    else:
        g=100000
        for j in range(dp[i-1],1,-1):
            if i%j==0 and (i//j)**(1/2)%1==0:
                g=j
                break
        if i in li2:
            g=min(g,2)
        if i in li3:
            g=min(g,3)
        dp.append(min(g,dp[i-1]+1))
#print(dp[n])
for i in range(1,n+1):
    print('%d : %d'%(i,dp[i]))