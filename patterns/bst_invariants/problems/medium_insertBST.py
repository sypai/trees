def insertBST(root, key):
    node = TreeNode(key)
    if not root:
        return node
    
    og_root = root
    
    while root:
        if root.val > key:
            if not root.left:
                root.left = node
                return og_root
            root = root.left
        elif root.val < key:
            if not root.right:
                root.right = node
                return og_root
            root = root.right
        else:
            return og_root