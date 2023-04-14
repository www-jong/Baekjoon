# dp실패
li=[0]+list(map(int,input().split()))
dp=[[[0,[0,0]],[0,[0,0]]] for i in range(len(li)+1)]
dp[1]=[[2,[li[1],0]],[2,[0,li[1]]]]
def check(x,y):
    if x==y:
        return 1
    elif x==0 or y==0:
        return 2
    elif abs(x-y)==2:
        return 4
    else:
        return 3
for i in range(1,len(li)):
    left_foot=[0,0]
    right_foot=[0,0]
    if dp[i-1][0][0]+check(li[i],dp[i-1][0][1][0])<dp[i-1][1][0]+check(li[i],dp[i-1][1][1][0]):
        dp[i][0]=[dp[i-1][0][0]+check(li[i],dp[i-1][0][1][0]),[li[i],dp[i-1][0][1][1]]]
    else:
        dp[i][0]=[dp[i-1][1][0]+check(li[i],dp[i-1][1][1][0]),[li[i],dp[i-1][1][1][1]]]

    if dp[i-1][0][0]+check(li[i],dp[i-1][0][1][1])<dp[i-1][1][0]+check(li[i],dp[i-1][1][1][1]):
        dp[i][1]=[dp[i-1][0][0]+check(li[i],dp[i-1][0][1][1]),[dp[i-1][0][1][0],li[i]]]
    else:
        dp[i][1]=[dp[i-1][1][0]+check(li[i],dp[i-1][1][1][1]),[dp[i-1][1][1][0],li[i]]]

print(min(dp[len(li)-2][0][0],dp[len(li)-2][1][0]))
'''
  1
2 0 4
  3
중앙 -> 사이드 : 2
사이드 -> 인접 : 3
사이드 -> 반대 : 4
같은지점 -> 1

dp[i][0]= [i번째에서 왼발일때 최소값,[왼,오]]
dp[i][1]= [i번째에서 오른발일때 최소값,[왼,오]]
'''