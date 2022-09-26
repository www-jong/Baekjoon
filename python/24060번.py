N,K=map(int,input().split())
li=list(map(int,input().split()))
def merge_srt(li):
    if li[0]<li[-1]:
        mid=len(li)//2
        merge_srt()