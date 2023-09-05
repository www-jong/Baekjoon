a=list(map(int,str(input())));a.sort(reverse=True);s=""
for i in range(len(a)):s+=str(a[i])
print(s)


#print(*sorted(input())[::-1],sep='')
#print(''.join(sorted(input()))[::-1])