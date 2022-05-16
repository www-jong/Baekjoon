import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
print(newstat)
print(*stat)
print('--------')
print(zip(*stat))
for i,j in zip(stat,zip(*stat)):
    print(i)
    print(j)