li=[]
while True:
    try:
        li.append(int(input()))
    except EOFError:
        break
print(li)

ltree=[i for i in range(len(li)+1)]
rtree=[i for i in range(len(li)+1)]


def func(node):
    global ltree,rtree    
    
func(li[0])