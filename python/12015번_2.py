N=int(input())
li=list(map(int,input().split()))
nowmax=li[0]
sample=[0]
maxlen=0
for i in range(len(li)):
    nownum=li[i]
    if sample[-1]<nownum:
        sample.append(nownum)
    else:
        left=0
        right=len(sample)
        while left<right:
            mid=(left+right)//2
            if sample[mid]<nownum:
                left=mid+1
            else:
                right=mid
        sample[right]=nownum
print(len(sample)-1)
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