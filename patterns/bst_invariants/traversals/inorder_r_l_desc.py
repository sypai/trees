# A right-root-left Inorder Traversal on a BST gives descending order
def ItInorder(root):
    if not root:
        return None
    
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.right
        
        current = stack.pop()
        print(current.val)

        current = current.left