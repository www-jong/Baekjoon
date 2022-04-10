from sys import stdin
from math import inf

n = int(stdin.readline())
m = int(stdin.readline())

cost = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1,n+1):
    cost[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

s=0
for row in cost:
    if s==0:
        s+=1
        continue
    for i in range(1,n+1):
        if row[i] == inf:
            row[i] = 0
        print(row[i], end=" ")
    print()