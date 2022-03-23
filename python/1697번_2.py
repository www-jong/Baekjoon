n,k=map(int,input().split())
dist=[0]*100001
for i in range(n+1,100000):
    if i%2==0:
        if dist[i+1]!=0:
            dist[i]=min(dist[i-1],dist[i//2],dist[i+1])+1
        else:
            dist[i]=min(dist[i-1],dist[i//2])+1
    else:
        if dist[i+1]!=0:
            dist[i]=min(dist[i-1],dist[i+1])+1
        else:
            dist[i]=dist[i-1]+1
    #print("%d :%d"%(i,dist[i]))
 
print(dist[k])



"""
다이나믹 프로그래밍으로 풀어보기 
시작지점은 n이다. 
dist[i]=min(dist[i-1]+1,dist[i//2]+1,dist[i+1]+1)


안되는거같다. 다시 돌아오는과정을 처리할 수가 없다.
"""