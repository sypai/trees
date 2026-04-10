def isDescendant(node, child):
    while node:
        if node.val > child.val:
            node = node.left
        elif node.val < child.val:
            node = node.right
        else:
            return True
    return False


def validateThreeNodes(nodeA, nodeB, nodeC):
    
    # Chain 1: nodeA -> nodeB -> nodeC
    chain1 = isDescendant(nodeA, nodeB) and isDescendant(nodeB, nodeC)

    # Chain 2: nodeC -> nodeB -> nodeA
    chain2 = isDescendant(nodeC, nodeB) and isDescendant(nodeB, nodeA)

    return chain1 or chain2


"""
        10
       /  \
      5    15
     / \     \
    2   7     20
"""
r = TreeNode(10)
r.left = TreeNode(5)
r.right = TreeNode(15)

r.left.left = TreeNode(2)
r.left.right = TreeNode(7)
r.right.right = TreeNode(20)

validateThreeNodes(r.left.left, r.left, r.right.right) # False