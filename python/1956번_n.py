# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
"""
동적계획법을 쓰고있었다;
V,E=map(int,input().split())
min=10000
road=[[0 for i in range(V+1)] for i in range(V+1)]
dp_fi=road
for i in range(E):
  a,b,c=map(int,input().split())
  road[a][b]=c
# 시작지점은 상관없다.
# 모든시작지점의 경우를 동적으로 계산해야된다.
for i in range(1,V+1):
    dp=[0 for s in range(V+1)]
    # dp[현재마을]=이동한거리
    for j in range(1,V+1):#처음 출발값 dp에 넣어주기
        dp[j]=road[i][j]
    while True:

                
print(min)
# -
"""
import sys
INF=100000000000
V,E=map(int,input().split())
road=[[INF for i in range(V)] for i in range(V)]

for i in range(E):
  a,b,c=map(int,sys.stdin.readline().split())
  road[a-1][b-1]=c
dp=road
for k in range(V):
    for s in range(V):
        for e in range(V):
            dp[s][e]=min(dp[s][k]+dp[k][e],dp[s][e])
min_val=INF
for i in range(V):
    for j in range(V):
        min_val=min(min_val,dp[i][j]+dp[j][i])
if min_val==INF:
    print('-1')
else:
    print(min_val)
'''
3 4
1 2 1
3 2 1
1 3 5
2 3 2
3
'''