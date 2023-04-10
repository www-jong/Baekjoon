for i in range(1,41):
    x=i*30
    print(f'{175*(1-0.995**(x))} {x}')
    
print(175*(1-0.995**(553)))