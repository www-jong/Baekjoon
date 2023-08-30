N=int(input())
fi=[0,1,1,2,3,5,8]
for i in range(5,3998):
    fi.append(fi[-1]+fi[-2])
print(fi[2*N-1]*N%100007)

# 피보나치수 관련문제. 논문봐야함