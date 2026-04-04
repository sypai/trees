"""
Given a binary tree, return the values of nodes visible from the right side. 
A node is visible from the right if it is the last node at its depth 
level when viewed from the right.
"""
from collections import deque

def right_profile(root):
    if not root:
        return []
    
    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level = []

        for _ in range(level_size):
            elem = q.popleft()
            level.append(elem.val)
            if elem.left:
                q.append(elem.left)
            if elem.right:
                q.append(elem.right)

        result.append(level[-1])
    return result