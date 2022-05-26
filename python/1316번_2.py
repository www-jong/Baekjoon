for _ in range(a:=int(input())):
 l=[]
 for i in (n:=input()):
  if i not in l:l.append(i)
  else:
   if i!=l[-1]:a-=1;break    
print(a)