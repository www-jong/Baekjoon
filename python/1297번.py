D,H,W=map(int,input().split())
S=(D**2/(H**2+W**2))**(0.5)
print(f'{int((H*S))} {int((W*S))}')