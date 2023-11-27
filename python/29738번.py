T=int(input())
for i in range(1,T+1):
    N=int(input())
    if N<=25:
        print(f'Case #{i}: World Finals')    
    elif N<=1000:
        print(f'Case #{i}: ROUND 3')
    elif N<=4500:
        print(f'Case #{i}: ROUND 2')
    else:
        print(f'Case #{i}: ROUND 1')

T = int(input())
for i in range(1, T+1):
    N = int(input())
    if N > 4500:
        print(f'Case #{i}: Round 1')
    elif N > 1000:
        print(f'Case #{i}: Round 2')
    elif N > 
        print(f'Case #{i}: Round 3')
    else:
        print(f'Case #{i}: World Finals')