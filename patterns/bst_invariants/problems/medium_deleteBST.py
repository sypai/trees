# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parentSet = [None, None]
        og_root = root
        while root:
            L = root.left
            R = root.right
            
            if root.val == key:
                # Leaf node
                if not L and not R:
                    
                    if not root == og_root:
                        if parentSet[1] == "L":
                            parentSet[0].left = None
                            return og_root
                        parentSet[0].right = None
                        return og_root
                    else:
                        return None
                    
                if L or R:
                    if not root == og_root:
                        if not L and R:
                            if parentSet[1] == "L":
                                parentSet[0].left = R
                                return og_root
                            parentSet[0].right = R
                            return og_root
                        if not R and L:
                            if parentSet[1] == "L":
                                parentSet[0].left = L
                                return og_root
                            parentSet[0].right = L
                            return og_root
                    else:
                        if not R:
                            return L
                        if not L:
                            return R
                
                if L and R:
                    if not root == og_root:
                        if parentSet[1] == "L":
                            parentSet[0].left = R
                            l = R
                            while l.left:
                                l = l.left
                            l.left = L
                            
                        elif parentSet[1] == "R":
                            parentSet[0].right = R
                            l = R
                            while l.left:
                                l = l.left
                            l.left = L
                    else:
                        og_root = R
                        l = R
                        while l.left:
                            l = l.left
                        l.left = L
                    
                    return og_root

            elif root.val > key:
                parentSet[0] = root
                parentSet[1] = "L"
                root = root.left
            else:
                parentSet[0] = root
                parentSet[1] = "R"
                root = root.right
        
        return og_root
    
