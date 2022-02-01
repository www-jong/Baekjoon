import time
start = time.time()  # 시작 시간 저장
 
 
# 작업 코드
m,n=map(int,input().split());l=[1]*(n+1)
for i in range(2,n+1):
 l[i::i]=[0]*(n//i)
 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간