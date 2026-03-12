def preorder(node):
    if node is None: 
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

