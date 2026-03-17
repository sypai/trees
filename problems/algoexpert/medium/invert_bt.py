def invert(node):
    if node is None:
        return
    invert(node.left)
    invert(node.right)
    temp = node.left
    node.left = node.right
    node.right = temp
    return node

from collections import deque

def invert_iterative(root):
    if root is None:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()

        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root