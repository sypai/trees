def isHeightBalanced(node):
    if bbt(node) == -1:
        return False
    return True

def bbt(node):
    if not node:
        return 0
    
    left = bbt(node.left)
    right = bbt(node.right)
    
    if left == -1 or right == -1:
        return -1
    
    if abs(left - right) > 1:
        return -1
    
    return 1 + max(left, right)