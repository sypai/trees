"""
Given a binary tree, find the maximum path sum. 
The path can start and end at any node in the tree — it does not need to pass through the root. 
A path is defined as a sequence of nodes where each pair of adjacent nodes has an edge. 
Each node can appear at most once. Node values can be negative.
""" 

### SOLUTION 1 - The Naive Solution I came up with 
# Time : O(n^2) | Space : O(n^2)
def maxPathSum(root):
    maxSum = [float("-inf")]

    def updateMaxSum(pathSum):
        if pathSum > maxSum[0]:
            maxSum[0] = pathSum

    def dfs(root):
        if not root.left and not root.right:
            updateMaxSum(root.val)
            return [root.val]
        
        if root.left:
            left = dfs(root.left)
        else:
            left = [0]
        
        if root.right:
            right = dfs(root.right)
        else:
            right = [0]

        for l in left:
            for r in right:
                updateMaxSum(l + r + root.val)
        
        return [x + root.val for x in [*left, *right]]
    
    dfs(root)
    return maxSum[0]

# This is my O(N) solution
def maxPathSum(root):
    maxSum = [float("-inf")]

    def updateMaxSum(pathSum):
        if pathSum > maxSum[0]:
            maxSum[0] = pathSum

    def dfs(root):
        if not root.left and not root.right:
            updateMaxSum(root.val)
            return root.val
        
        if root.left:
            left = dfs(root.left)
        else:
            left = 0
        
        if root.right:
            right = dfs(root.right)
        else:
            right = 0

     
        updateMaxSum(left + right + root.val)
        
        return max(root.val, root.val + max(left, right))
    
    dfs(root)
    return maxSum[0]
    
# This is the Optimised solution 
# T : O(N) | Space : O(h)
def maxPathSum(root):
    maxSum = [float("-inf")]

    def dfs(node):
        if not node:
            return 0
        
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        maxSum[0] = max(maxSum, left + right + node.val)

        return node.val + max(left, right)

    return maxSum[0]