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
g=0
count=0
for i in range(int(input())):
    g=0
    strr=list(input())
    arr=[0 for j in range(26)]
    arr[ord(strr[0])-97]=1
    for j in range(1,len(strr)):
        if arr[ord(strr[j])-97]==1 and strr[j]!=strr[j-1]:
            arr[ord(strr[j])-97]=0  # 이미, 나온단어인데 연속되지않다면
            g=1
        if arr[ord(strr[j])-97]==0: #한번도 안나온 단어라면
            arr[ord(strr[j])-97]=1
    if g==0:count+=1
print(count)


#숏코딩
#print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)

#r=0;exec("s=input();r+=all(s.find(c*s.count(c))+1for c in s);"*int(input()));print(r)

#res=0
#for i in range(int(input())):
#    s=input()
#    res+=list(s) == sorted(s,key=s.find)
#print(res)

# sorted(s,key=s.find) 는 요약하자면
# 기존순서를 유지한채로 정렬하는걸로 보인다.
# aabb 같은경우 그대로, aabba같은경우 정렬당한다. 그래서 같지않게되면res가 +=되지않는다
# -





