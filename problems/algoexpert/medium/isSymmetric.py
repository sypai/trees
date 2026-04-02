def is_mirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if not left.val == right.val:
        return False
    
    return is_mirror(left.left, right.left) and is_mirror(left.right, right.left)

def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)