"""
Given a BST and a target value, find the value in the BST that is 
closest to the target. Guaranteed exactly one answer.

        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
    
target = 11
Output = 10
"""

def closestToBST(root, target):
    closest = [float("inf"), None]

    def dfs(root):
      if not root:
            return None
      
      val = root.val
      diff = abs(val - target)
      if diff == 0:
          closest[0] = 0
          closest[1] = val
      if val < target: 
          if closest[0] > diff:
              closest[0] = diff
              closest[1] = root.val
          dfs(root.right)
      else:
          if closest[0] > diff:
              closest[0] = diff
              closest[1] = root.val
          dfs(root.left)
    dfs(root)
    return closest[1]


def cleanedUpClosestToBST(root, target):
    closest = [float("inf"), None]

    def dfs(node):
        if not node: return
        
        diff = abs(node.val - target)
        if diff < closest[0]:
            closest[0] = diff
            closest[1] = node.val
        
        if target < node.val:
            dfs(node.left)
        elif target > node.val:
            dfs(node.right)
        # diff == 0 case: neither branch taken, recursion stops naturally
    
    dfs(root)
    return closest[1]

# Option 4 — iterative, no global state at all
def closestBST(root, target):
    closest = root.val
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            return root.val
    return closest

