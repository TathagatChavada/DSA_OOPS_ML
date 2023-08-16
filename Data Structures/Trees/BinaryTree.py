class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.item = value
        
    
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    
    print(str(root.item) + "---->", end = '')
    
    inorder(root.right)
    
    
def preorder(root): 
    if root is None:
        return
    
    print(str(root.item) + "---->", end = '')
    
    preorder(root.left)
    
    preorder(root.right)
    
    
def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    
    postorder(root.right)
    
    print(str(root.item) + "---->", end = '')
    
    
    
def Is_Full_Tree(root):
    if root is None:
        return True
    
    elif (root.left is None) and (root.right is None):
        return True
    
    elif (root.left is not None) and (root.right is not None):
        return Is_Full_Tree(root.left) and Is_Full_Tree(root.right)
    
    else:
        return False



def inorder_iterative(root):
    res = []
    stack = []
    curr = root
    
    while curr or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        res.append(curr.item)
        
        curr = curr.right
        
    print(res)
            

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal")
inorder(root)  
print('\n')

print("Preorder Traversal")
preorder(root)  
print('\n')

print("Postorder Traversal")
postorder(root)  
print('\n')
 
 
print(f"Is Full Binary Tree: {Is_Full_Tree(root)}")
# inorder_iterative(root)