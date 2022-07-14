import sys
input=sys.stdin.readline
n=int(input())
li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1])

count=1
end=li[0][1]
for i in range(1,n):
    if li[i][0]>=end:
        count+=1
        end=li[i][1]
print(count)
'''
시작시간을 오름차순으로 정렬 후, 종료시간을 오름차순 정렬
-->
3-3 2-3 1-3 2-4 1-5 4-5 5-5 3-5 3-4 4-4
-> 1-3 1-5 2-3 2-4 3-3 3-5 3-4 4-5 4-4 5-5 (시작시간오름차순)
-> 1-3 2-3 3-3 2-4 3-4 4-4 1-5 3-5 4-5 5-5
시작시간이 같으면 종료시간이 낮은순이 아니라, 시작시간 오름차순 기반으로
2-5보다 3-4가 앞으로 당겨져 옴
'''