# 접근법
# st, end를 처음과 끝으로두고
# li[st]와 li[end]중 작은 것을 총합이 S가 넘는 수준에서 제외
# 하지만, 양옆이 같은경우에서 복잡해져서 망함

N,S=map(int,input().split())
li=list(map(int,input().split()))
now=sum(li)
res=10**9
st,end=0,N-1
while st<end:
    if now>=S:
        if li[st]>li[end]:
            if now-li[end]>=S:
                now-=li[end]
                end-=1
            else:
                break
        elif li[st]<li[end]:
            if now-li[st]>=S:
                now-=li[st]
                st+=1
            else:
                break
        else:
            t_st=st+1
            t_end=end-1
            while t_st<t_end:
                if li[t_st]<li[t_end]:
                    if now-li[st]>=S:
                        now-=li[st]
                        st+=1
                    else:
                        break                    
                elif li[t_st]>li[t_end]:
                    if now-li[end]>=S:
                        now-=li[end]
                        end-=1
                    else:
                        break
                else:
                    t_st+=1
                    t_end-=1
    else:
        break

print(0 if (end-st+1)==len(li) and sum(li)<S else end-st+1)