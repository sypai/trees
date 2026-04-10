"""
Interview trap: "Validate a BST" is almost always failed by people who only check node vs. its immediate 
children. 
You must propagate min/max bounds down the tree.


LOL I fell for the same thing! I ran confidently thinking my recursive soln was correct - but I was just
checking immediate l and r
"""

# CORRECT Check against min and max limits
def isValid(root, min, max):
    if not root:
        return True
    
    left = isValid(root.left, min, root.val)
    right = isValid(root.right, root.val, max)
    
    if min < root.val < max:
        return left and right
    return False
    

def validateBST(root):
    return isValid(root, float("-inf"), float("inf"))



### Incorrect
def isValidBST(root) -> bool:
        if not root:
            return True
        
        if root.right:
            if root.val >= root.right.val:
                return False
        if root.left:
            if root.val <= root.left.val:
                return False 
        
        left = isValidBST(root.left)
        right = isValidBST(root.right)
        
        return left and right