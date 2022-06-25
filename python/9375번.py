for _ in range(int(input())):
    n=int(input())
    dic={}
    if n!=0:
        for i in range(n):
            s,g=input().split()
            if g in dic:
                dic[g]+=1
            else:
                dic[g]=1
        ans=1
        for i in dic.keys():
            ans*=(dic[i]+1)
        print(ans-1)
    else:
        print(0)