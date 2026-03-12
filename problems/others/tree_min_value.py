"""
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""
from collections import deque

def tree_min_value(rootNode):
    minimum = float("inf")
    queue = deque([rootNode])

    while queue:
        curr = queue.popleft()
        if curr.val < minimum:
            minimum = curr.val
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        
    return minimum


def tree_min_recr(rootNode):
    if rootNode is None:
        return float("inf")
    left = tree_min_recr(rootNode.left)
    right = tree_min_recr(rootNode.right)
    return min(left, right, rootNode.val)
