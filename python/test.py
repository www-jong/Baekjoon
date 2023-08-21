def cal_time(Can, D, rule, i):
    if Can[i] == 1:
        return D[i]
    
    else:
        x_time = []
        for x in rule[i]:
            D[x] = cal_time(Can, D, rule, x)
            Can[x] = 1
            x_time.append(D[x])

        return max(x_time) + D[i]

import sys

T = int(sys.stdin.readline())

for _ in range(T):            
    # N : 건물의 개수 / K : 건설순서 규칙의 총 개수
    N, K = map(int, sys.stdin.readline().split())

    # Can : 각 건물이 건설 가능하다면 1 아니면 0 으로 체크하는 list (index는 건물 숫자와 동일하다)
    Can = [1] * (N + 1)
        
    # D : 각 건물 당 건설에 걸리는 시간 list
    D = [0] + list(map(int, sys.stdin.readline().split()))
    # rule : 건설순서 규칙 rule[Y] = [X1, X2, X3, ...] -> X1, X2, X3, ...를 모두 건설해야 Y를 건설가능
    rule = {i: [] for i in range(1, N + 1)}

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        Can[Y] = 0
        rule[Y].append(X)
    # W : 건설해야 할 건물의 번호
    W = int(sys.stdin.readline())

    print(cal_time(Can, D, rule, W))