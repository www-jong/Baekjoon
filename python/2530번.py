a,b,c=map(int,input().split())
m=(a*3600+b*60+c+int(input()))%86400
print("%d %d %d"%(m//3600,m%3600//60,m%60))