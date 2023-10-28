while True :
    try :
        s = list(input())
        lower , upper, num, blank = 0,0,0,0
        for i in range(len(s)) :
            if s[i] == " " :
                blank += 1
            elif 65 <= ord(s[i]) <= 90 :
                upper += 1
            elif 97 <= ord(s[i]) <= 122 :
                lower += 1
            else :
                num += 1
        print(lower,upper,num,blank)
    except EOFError :
        break