for _ in range(int(input())):
    S=input()
    ans=1
    check=1
    for i in range(len(S)):
        if (i+1)>(len(S)+1)//2:
            break
        else:
            if S[i]!=S[len(S)-i-1]:
                check=0
                break
        ans+=1
    print("%d %d"%(check,ans if check==0 else (ans if len(S)%2==0 else ans-1)))