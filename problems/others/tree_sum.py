"""
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.
"""
from collections import deque

def tree_sum(node):
    if node is None:
        return 0
    return tree_sum(node.left) + tree_sum(node.right) + node.val

def tree_sum_bfs(node):
    if node is None:
        return 0
    sum = 0
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        sum += curr.val
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return sum