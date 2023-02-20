N=int(input())
tree=[0]*(N+1)
left_tree=[0]*(N+1)
right_tree=[0]*(N+1)

for i in range(1,N+1):
    t,l,r=map(str,input().split())
    tree[ord(t)-64]=t
    left_tree[ord(t)-64]=ord(l)-64 if l!="." else "."
    right_tree[ord(t)-64]=ord(r)-64 if r!="." else "."
def preorder(x):
    res=tree[x]
    if left_tree[x]!=".":res+=preorder(left_tree[x])
    if right_tree[x]!=".":res+=preorder(right_tree[x])
    return res    

def inorder(x):
    res=""
    if left_tree[x]!=".":res+=inorder(left_tree[x])
    res+=tree[x]
    if right_tree[x]!=".":res+=inorder(right_tree[x])
    return res    
def postorder(x):
    res=""
    if left_tree[x]!=".":res+=postorder(left_tree[x])
    if right_tree[x]!=".":res+=postorder(right_tree[x])
    res+=tree[x]
    return res    

print(preorder(1))
print(inorder(1))
print(postorder(1))