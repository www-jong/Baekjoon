k=float(input())
g=float(input())
print('Overweight' if k/(g*g)>=25 else ('Normal weight' if k/(g*g)>=18.5 else 'Underweight'))