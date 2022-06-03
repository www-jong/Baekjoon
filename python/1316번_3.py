n=int(input())
d=n
for _ in range(n):
   word=input()
   li=[]
   now=''
   for i in word:
      if i not in li:
         li.append(i)
         now=i
      else:
         if i!=now:
            d-=1
            break
print(d)