def bstFromPreorder(self, preorder):
    if not preorder:
        return None
    
    root = TreeNode(preorder[0])
    
    split = len(preorder)  # default: all remaining go left
    for i in range(1, len(preorder)):
        if preorder[i] > preorder[0]:
            split = i
            break
    
    root.left  = self.bstFromPreorder(preorder[1:split])
    root.right = self.bstFromPreorder(preorder[split:])
    return root