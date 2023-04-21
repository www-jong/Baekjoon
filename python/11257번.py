T=int(input())
for i in range(T):
    A,B,C,D=map(int,input().split())
    res='FAIL' if B<30*0.35 or C<30*0.25 or D<30*0.4 or B+C+D<55 else 'PASS'
    print(f'{A} {B+C+D} {res}')