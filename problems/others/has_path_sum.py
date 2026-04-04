def hasPathSum(root, target):
    if not root:
        return False
    
    revisedTarget = target - root.val

    # What if there are negative integers
    # if revisedTarget < 0:
    #     return False 
    
    if not root.left and not root.right:
        return revisedTarget == 0
    
    return hasPathSum(root.left, revisedTarget) or hasPathSum(root.right, revisedTarget)