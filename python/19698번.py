N,W,H,L=map(int,input().split())
r=min((W//L)*(H//L),N)
print(r)