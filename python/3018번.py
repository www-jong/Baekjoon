N=int(input())
E=int(input())
graph=[set() for i in range(N+1)]
for i in range(E):
    li=list(map(int,input().split()))
    if 1 in li[1:]:
        for j in li[1:]:
            graph[j].add(i)
    else:
        total=set()
        for j in li[1:]:
            total=total.union(graph[j])
        for j in li[1:]:
            graph[j]=graph[j].union(total)

for i in range(1,N+1):
    if len(graph[i])==len(graph[1]):
        print(i)