# Time : O(n)| Space: O(n)
def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums

def calculate_branch_sums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.val
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculate_branch_sums(node.left, newRunningSum, sums)
    calculate_branch_sums(node.right, newRunningSum, sums)