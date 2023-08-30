S=input()
a,b=S.count(':-)'),S.count(':-(')
print(("none"if a==0 else "unsure") if a==b else("happy"if a>b else "sad"))