H,W,N,M = list(map(int,input().split(' ')))
import math
a = math.ceil(H/(N+1))
b = math.ceil(W/(M+1))
answer = a*b
print(answer)