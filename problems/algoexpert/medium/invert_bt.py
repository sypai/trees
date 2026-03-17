def invert(node):
    if node is None:
        return
    invert(node.left)
    invert(node.right)
    temp = node.left
    node.left = node.right
    node.right = temp
    return node