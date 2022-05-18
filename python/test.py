def make_table(pat):
    length=len(pat)
    table=[0]*length
    j=0

    for i in range(1,length):
        while j>0 and pat[i]!=pat[j]:
            j=table[j-1]
        if pat[i]==pat[j]:
            j+=1
            table[i]=j
    return table

def kmp(txt,pat):
    table=make_table(pat)
    txt_len=len(txt)
    pat_len=len(pat)
    j=0
    for i in range(txt_len):
        while j>0 and txt[i]!=pat[j]:
            j=table[j-1]
        if txt[i]==pat[j]:
            if j==pat_len-1:
                return 1
            else:
                j+=1
    return 0
txt=input()
pat=input()
print(kmp(txt,pat))