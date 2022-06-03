a=input()
s=eval(a.replace("A","4").replace("B","3").replace("C","2").replace("D","1").replace("F","0").replace("+","+0.3").replace("-","-0.3"))
print(f"{s:.1f}" if s<10 else s/10)
