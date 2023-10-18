'''#depth first search
inoder
preoder
postoder
'''
class node:
    def __init__(self,data) -> None:
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    print(root.val)
    printing(root.left)
    printing(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.right.right=node(5)
printing(root)
#level oder traversal
q=[]
q.append(root)
while q:
    a=q.pop(0)
    #print(a.val)
    if a.left:
        q.append(a.left)
        print(a.left.val)
    if a.right:
        q.append(a.right)
