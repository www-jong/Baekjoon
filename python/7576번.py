import sys
from collections import deque

x,y=map(int,input().split())
graph=[]
visited=[[0]*(x+1) for i in range(y+1)]
for i in range(y):
    graph.append([0]+list(map(int,input().split())))
if sum(graph)==x*y:
    print(0)
else:
    for aa in range(x+1):
        for bb in range(y+1):
            q=deque()