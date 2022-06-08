while True:
    n=input()
    if n=="." or n=="..":
        break
    while n[-1]!=".":
        n+=input()
    c=["(",")","[","]"]
    n_li=""
    for i in n:
        if i in c:
            n_li+=(i)
    while n_li.count("[]")+n_li.count("()")>0:
        n_li=n_li.replace("[]","").replace("()","")
    n_li=list(n_li)
    check=0
    if len(n_li)>0:
        print("no")
    else:
        print("yes")