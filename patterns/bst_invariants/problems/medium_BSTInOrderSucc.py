def inorderSuccessor(root, node):
    successor = None
    
    while root:
        if node.val < root.val:
            # Current root is a potential successor because it's larger than node
            successor = root
            root = root.left
        elif node.val > root.val:
            # Current root is smaller, so successor must be in the right subtree
            # We do NOT reset successor to None here
            root = root.right
        else:
            # We found the node!
            if root.right:
                # If there's a right child, the successor is the leftmost node of that subtree
                current = root.right
                while current.left:
                    current = current.left
                return current
            else:
                # If no right child, the last 'left turn' we took is the successor
                return successor
                
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
