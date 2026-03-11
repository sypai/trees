"""
Depth First Search (DFS) — Preorder Traversal (Iterative)

Traversal Order:
    node → left → right

Key Idea:
    Use an explicit stack to simulate the recursion call stack.

Algorithm:
    1. Initialize stack with root node.
    2. Pop node from stack.
    3. Visit the node.
    4. Push right child to stack.
    5. Push left child to stack.
       (Left is pushed last so it is processed first due to LIFO behavior.)

Time Complexity:
    O(n) — every node is visited exactly once.

Space Complexity:
    O(h) average, O(n) worst case
    where h = height of tree (stack stores ancestor path).

When to Use:
    - Tree traversal
    - Searching nodes
    - Base pattern for many tree problems

Important Insight:
    Recursive DFS → uses call stack.
    Iterative DFS → uses explicit stack.
"""
from collections import deque

# Time : O(N), Space: O(N)
def dfs_preorder(node):
    if node is None:
        return
    stack = []
    stack.append(node)

    while len(stack) > 0: # is stock non-empty
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        

def dfs_preorder_deque(root):
    if root is None:
        return []

    stack = deque([root])


    while stack:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
