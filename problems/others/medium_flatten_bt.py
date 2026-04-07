# This was my solution with a lot of flaws but it worked for the tree I started writing code for
def flatten(root):
    if not root:
        return None
    
    if root.left:
        tail = flatten(root.left)
        root.left = None
    else:
        return root
    
    if tail:
        if root.right:
            temp = root.right
            root.right = root.left
            root.left = None
            tail.right = temp
            tail = flatten(temp)
        else:
            root.right = tail
            return tail


# AND THIS IS THE ONE LLMs taught me
# Here's the simple rule for Postorders Suyash, left, right, do whatever you have to at root and return
def flatten(root):
    if not root:
        return None
    
    left_tail = flatten(root.left)
    right_tail = flatten(root.right)

    if root.left:
        temp = root.right
        root.right = root.left
        left_tail.right = temp
        root.left = None

    return right_tail or left_tail or root

