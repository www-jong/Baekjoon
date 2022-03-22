import math
def g(li):
    gc=0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            gc+=(math.gcd(li[i],li[j]))
    return gc

t=int(input())
for i in range(t):
    a=list(map(int,input().split()))[1:]
    print(g(a))

"""
문제설명이 빈약하다.
10 20  30 40 이 주어지면,
gcd(10,20)=10, gcd(10,30)=10 , ... gcd(30,40)=10 을 다 합친값을 출력한다.
"""