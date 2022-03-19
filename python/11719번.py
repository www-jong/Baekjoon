c=""
while c!=".":
    c=input()
    sco=0
    mco=0
    for i in c:
        if i=="[":
            mco+=1
        elif i=="(":
            sco+=1
        elif i=="]":
            mco-=1
        elif i==")":
            sco-=1
    if sco!=0 or mco!=0:
        print("no")
    else:
        print("yes")