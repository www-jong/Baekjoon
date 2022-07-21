
a,b=map(int,input().split())
a=list(reversed(list(str(a))))
b=list(reversed(list(str(b))))
a=int(''.join(a))
b=int(''.join(b))
print(max(a,b))

#숏코딩예제들
#print(max(input()[::-1].split()))
#이런...방법이
#a b 입력했을때, a를 뒤집고, b를 뒤집고 분리해서..?
#abc def 를 fed cba 로 뒤집고, 분리해서 크기비교..
