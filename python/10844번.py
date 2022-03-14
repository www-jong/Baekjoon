"""
# 테스트용, 백트래킹
n=int(input())
arr=[]
count=0
def func():
    global count
    if len(arr)==n:
        count+=1
        print(*arr,sep="",end=" ")
        return
    for i in range(10):
        if i==0 and len(arr)==0:
            continue
        elif len(arr)==0:
            arr.append(i)
            func()
            arr.pop()
        else:
            c=arr.pop()
            if abs(i-c)==1:
                arr.append(c)
                arr.append(i)
                func()
                arr.pop()
            else:
                arr.append(c)
func()
print("\ncount : %d"%(count))
"""
"""
------------------------


테스트용으로 백트래킹으로 나올 수 있는 수들을 체크해봤다.
백트래킹으로는 당연하게도 n이 100일때까지는 무리다. 
n = 1
1 2 3 4 5 6 7 8 9 --> 9

n = 2
10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98 --> 17

n = 3
101 121 123 210 212 232 234 321 323 343 345 432 434 454 456 543 545 565 567 654 656 676 678 765 767 787 
789 876 878 898 987 989 --> 32

n = 4
1010 1012 1210 1212 1232 1234 2101 2121 2123 2321 2323 2343 2345 3210 3212 3232 3234 3432 3434 3454 3456 
4321 4323 4343 4345 4543 4545 4565 4567 5432 5434 5454 5456 5654 5656 5676 5678 6543 6545 6565 6567 6765 
6767 6787 6789 7654 7656 7676 7678 7876 7878 7898 8765 8767 8787 8789 8987 8989 9876 9878 9898        
--> 61

n = 5
--> 116

n = 6
--> 222

 1  2  3  6  10  20  35   70  126
9 17 32 61 116 222 424 813 1556 2986 5721 10982 21053 40416 77505
 8 15 29 55 106
  7 14 26 51
 
단순하게규칙만 보면
s[i]=s[i-1]+i
dp[i]=dp[i-1]+ s[i]

근데 이것도 규칙이 이후엔 틀리다. 

dp[i-1]에서 0 또는 9로 끝나는 경우, dp[i]에서 1번씩의 경우가 빠진다.
그러므로, 마지막 숫자가 0 또는 9인 s배열을 만든다.
s[1] = 9
s[2] = 10 89
s[3] = 210 789 989
s[4] = 3210 1210 1010 6789 8789 8989
s[5] = 43210 23210 21210 21010 56789 76789 78789 98789 98989 78989

이것도 규칙이 따로 안보이므로, 시작하는 숫자가 1 또는 9인 것을 찾는다
s[1] = 9
s[2] = 10 12 98
s[3] = 123 121 101 987 989
... s[i]에서 1로끝나는경우 -> 12x와 10x 존재 --> dp[i-1]에서 2, 0(이건 dp[i-2]에서 1로 끝나는경우와 동일) 으로 끝나는경우
             9로 끝나는 경우 98x 존재  --> dp[i-1]에서 8로끝나는경우

...

그러면 dp[i]=dp[i-1]*2-s[i-1]
여기서 s[i]는 9또는 1로 시작하는 i자리수
---> dp[i][j] 로 바꾼다. 복잡해지므로,
dp[i][j]= i자리수인데 j로 시작하는 수

즉, sum(dp[i])= i자리수의 계단수 갯수
dp[i][1]= dp[i-1][2]+dp[i-2][1] 
--> 1xxx...일때, 12xxx 와 101xx가 되므로
dp[i][9]= dp[i-1][8]
--> 9xxx 일때, 98xx 가 있으므로, 
"""

n=int(input())
dp=[[0]*10 for i in range(n+1)]
for i in range(1,10):
    dp[0][i]=1
    dp[1][i]=1
for i in range(2,n+1):
    dp[i][1]=dp[i-1][2]+dp[i-2][1]
    dp[i][9]=dp[i-1][8]
    for j in range(2,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(int(sum(dp[n])%1000000000))
