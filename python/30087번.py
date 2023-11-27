N=int(input())
r=''
d=['Algorithm','DataAnalysis','ArtificialIntelligence','CyberSecurity','Network','Startup','TestStrategy']
f=[204,207,302,'B101',303,501,105]
for i in range(N):
    s=input()
    for j in range(7):
        if d[j]==s:
            print(f[j])
            break