def lca(root, p, q):
    if not root:
        return None
    
    val = root.val

    if val == p:
        return root
    if val == q:
        return root
    
    if val < p and val > q:
        return root
    elif val > p and val < q:
        return root
    
    if val > p and val > q:
        left = lca(root.left, p, q)
        if left:
            return left
    if val < p and val < q:
        right = lca(root.right, p, q)
        if right:
            return right
    
    return None

    
def lcaIt(root, p, q):
    if not root:
        return None
    
    while root:
        if root.val < p and root.val < q:
            root = root.right
        if root.val > p and root.val > q:
            root = root.left
        else:
            return root.val
