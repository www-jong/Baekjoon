idx=1
while  True:
    L,P,V=map(int,input().split())
    if L==0:
        break
    if V%P>L:
        print(f'Case {idx}: {L*(V//P)+(L)}')
    else:
        print(f'Case {idx}: {L*(V//P)+(V%P)}')
    idx+=1