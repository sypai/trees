"""
You are given two binary trees.

Write a function that merges them into a single tree.

Rules:

If two nodes overlap → sum their values

If only one node exists → use that node

Structure should be preserved

Solution - 

I start w the root nodes

and also create a new tree along the way

node1 = rootA
node2 = rootB

if node1 and node2:
        newNode = node1.val + node2.val

while node1 and node2:
    node1 = node1.left
    node2 = node2.left
"""
from collections import deque

def merge(rootA, rootB):
    if rootA is None and rootB is None:
        return None
    if rootA is None:
        return rootB
    elif rootB is None:
        return rootA
        
    stackA = deque([rootA]) 
    stackB = deque([rootB]) 

    # # we decide we'll return the rootA - so we merge trees in place of nodes of tree repr by rootA
    # rootA.val = rootA.val + rootB.val

    while stackA and stackB:
        nodeA = stackA.popleft()
        nodeB = stackB.popleft()

        nodeA.val = nodeA.val + nodeB.val

        if nodeA.left is not None and nodeB.left is not None:
            stackA.append(nodeA.left)
            stackB.append(nodeB.left)
        if nodeA.right is not None and nodeB.right is not None:
            stackA.append(nodeA.right)
            stackB.append(nodeB.right)

        if nodeA.left is None and nodeB.left is not None:
            nodeA.left = nodeB.left
        if nodeA.right is None and nodeB.right is not None:
            nodeA.right = nodeB.right

    return rootA
        



# def dfs_preorder_deque(root):
#     if root is None:
#         return []

#     stack = deque([root])
#     preorder = []

#     while stack:
#         node = stack.pop()
#         print(node.val)

#         if node.right:
#             stack.append(node.right)
#             preorder.append(node.right.val)
#         else:
#             preorder.append(None)

#         if node.left:
#             stack.append(node.left)
#             preorder.append(node.left.val)
#         else:
#             preorder.append(None)

#     return preorder