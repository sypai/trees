# A left-root-right Inorder Traversal on a BST gives ascending order
def ItInorder(root):
    if not root:
        return None
    
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        print(current.val)

        current = current.right
