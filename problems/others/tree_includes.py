"""
Write a function, treeIncludes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.
https://structy.net/problems/tree-includes
"""
from collections import deque

def tree_includes(node, target):
    if node is None:
        return False
    if node.val == target:
        return True
    
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        if curr.val == target:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return False

def tree_includes_dfs(node, target):
    if node is None:
        return False
    if node.val == target:
        return True
    return tree_includes(node.left, target) or tree_includes(node.right, target)
