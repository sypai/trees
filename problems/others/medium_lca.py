def lca(root, p, q):
    if not root:
        return None
    
    if root.val == p:
        return root
    if root.val == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    
    if left:
        return left
    if right:
        return right
    return None

def LCA(root, p, q):
    return lca(root, p, q).val

"""
Left found something, right found something → current node is LCA
Only left found something → return left result upward
Only right found something → return right result upward
Neither found anything → return null
"""