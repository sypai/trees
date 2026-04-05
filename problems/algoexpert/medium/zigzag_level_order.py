"""
Zig Zag Level Order traversal
"""
from collections import deque

def zigzag(root):
    if root is None:
        return []
    
    q = deque([root])
    zig = False
    result = []

    while q:

        level_size = len(q)
        level = deque([])

        for _ in range(level_size):
            node = q.popleft()
            if zig:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append([*level])
        zig = not zig

    return result
    