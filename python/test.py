for i in range(1,26):
    r=i//5+(0 if i%5==0 else 1)
    c=i%5+(5 if i%5==0 else 0)
    print(f'{r} : {c}')