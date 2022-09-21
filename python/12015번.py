N=int(input())
li=list(map(int,input().split()))
nowmax=li[0]
comax=1
dp=[{} for i in range(N)]

for i in range(N):
    if i==0:
        dp[i]={li[i]:1}
    else:
        checker=0
        for val in dp[i-1].keys():
            if val<li[i]:
                print("%d %d %d -> %d"%(i,val,li[i],dp[i-1][val]+1))
                dp[i][li[i]]=max(dp[i-1][val],dp[i][li[i]]-1 if li[i] in dp[i] else 0)+1
                checker=1
            else:
                print("... %d %d %d"%(i,val,max(dp[i-1][val],dp[i][val] if val in dp[i] else 0)))
                dp[i][val]=max(dp[i-1][val],dp[i][val] if val in dp[i] else 0)
        if checker==0:
            if li[i] in dp[i]:
                pass
            else:
                dp[i][li[i]]=1
maxval=0
for i in dp[N-1].values():
    if maxval<i:
        maxval=i
print(i)
print(dp)

'''
1 5 4 2 3 6 1 4 2 10
'''




'''
for i in range(1,N+1):
    for j in range(i):
        if li[j]<li[i] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))
'''

def binary_search(target,data):
	data.sort() # 오름차순으로 정렬되어야 함
	start=0
	end=len(data)-1 # 시작과 끝은 배열의 0과 마지막인덱스
	
	while start<=end:
		mid= (start+end)//2
		if data[mid]==target:
			return mid # 종료조건
		elif data[mid]<target: # 목표값이 오른쪽에 있는경우
			start=mid+1
		else:
			end=mid-1 # 목표값이 왼쪽에 있는경우
	return