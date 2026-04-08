"""
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/?envType=problem-list-v2&envId=tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        sums = []

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            sums.append(level_sum)
        
        if len(sums) < k:
            return -1

        sums.sort()
        return sums[-k]

