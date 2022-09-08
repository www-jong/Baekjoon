N=int(input())
k=int(input())

start=0
end=N*N
ans=0
while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(1,N+1):
        count+=N if (mid//i)>N else mid//i
    if count>=k:
        ans=mid
        end=mid-1
    elif count<k:
        start=mid+1
print(ans)

'''
모든 수를 구할 필요없이, k번째 인덱스 까지만 알면 됨
mid보다 작은 수의 갯수를 구함(count)
이때, count가 k와 같으면 그것이 정답.
k보다 count가 작으면, mid를 더 높임(start=mid+1)
반대로, k가 count보다 작으면 mid를 더 낮춤(end=mid-1)
근데 이때, 아래의 경우가 존재할 수 있음
N=3 일때,
1 2 2 3 3 4 6 6 9
여기서 현재 3인 숫자를 탐색중인 경우,
k는 4, 5 두개가 될 수 있음

좀더 크게 보면,
N이 큰수(대충 100000) 일때,
특정 인덱스 구간 a~b(a<=k<=b) 가 전부 같은 숫자c를 가지고 있을 수 있음
가령, 리스트 B= 1,2,3,4,5,5,5,5,5,5,5,5,5,6,9 일때,
인덱스 5부터 13은 다 같은 숫자값을 가짐
k=8을 찾고자 할 때,
mid= 4부터 시작할 경우, count는 3 이고  count<k이므로 mid를 높임
mid (5+9)//2=6 일 경우, count는 13 이고, count>k이므로 mid를 낮춤. 그런데,
이론상 정답과 mid가 같으므로 이런 경우, ans=mid 처리를 해주어야 함
물론 틀릴수도 있지만, 바로 return하지 않고 가장 정확한 위치로 계속 나아가므로 상관없음
mid (4+5)//2=4 일 경우, count는 3 이고 count<k 이므로 mid를 높임
mid (5+5)//2=5 일 경우, count는 4 이고 count<k 이지만, start==end이므로 빠져나감
결국 ans는 5를 가지게 됨. 
'''