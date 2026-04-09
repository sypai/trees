def inorderSuccessor(root, node):
    if not root:
        return None
    
    successor = None

    while root:
        if root is node:
            if root.right:
                current = root.right
                while current.left:
                    current = current.left
                return current
            else:
                return successor
        else:
            if root.val > node.val:
                successor = root
                root = root.left
            else:
                successor = None
                root = root.right
    return successor

"""
          5
         / \
        3   6
       / \
      2   4
     /
    1
"""
# of 2
inorderSuccessor(root, root.right)   
