def splitTree(root):
    def totalSum(node):
        if not node:
            return 0
        return node.val + totalSum(node.left) + totalSum(node.right)

    total = totalSum(root)

    if total % 2 != 0:
        return False

    target = total // 2
    found = False

    def dfs(node):
        nonlocal found

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        subtree_sum = node.val + left + right

        if subtree_sum == target and node != root:
            found = True

        return subtree_sum

    dfs(root)

    return found