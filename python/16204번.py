N,M,K=map(int,input().split())
ox=[N-M,M]
print(min(ox[0],N-K)+min(ox[1],N-N+K))