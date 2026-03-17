def diameterOfBinaryTree(self, root):
        d = [0]
        self.find_diameter(root, d)
        return d[0]
    
def find_diameter(self, root, d):
    if root.left is None and root.right is None:
        return 0
    r_l, r_r = 0, 0
    if root.left:
        r_l = self.find_diameter(root.left, d) + 1
    if root.right:
        r_r = self.find_diameter(root.right, d) + 1
    if d[0] < r_r + r_l:
        d[0] = r_r + r_l
    return max(r_r, r_l)