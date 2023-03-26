while True:
    try:
        N=input()
        if N=='':
            break
        else:
            bar='-'
            empty=' '
            res='-'
            for i in range(int(N)):
                res=res+empty+bar
                bar=res
                empty=empty*3
            print(res)
    except EOFError:
        break