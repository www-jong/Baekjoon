a=[[2,5],[1,4],[1,8],[1,5],[2,1],[1,3],[3,1],[4,7],[5,4]]
#a.sort(key=lambda x:(x[0],x[1]))
a.sort(key=lambda x:(x[0],-x[1]))
a.sort(key=lambda x:x[0])
print(a)