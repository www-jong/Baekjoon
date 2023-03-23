a,b,c,d,e,f=map(int,input().split())
print(f'{int((e*c-f*b)/(a*e-b*d))} {int((c*d-a*f)/(b*d-e*a))}')