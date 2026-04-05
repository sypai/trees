from collections import deque

def itInorder(root):
    if not root:
        return []
    inorder = []
    
    stack = deque([root])
    seen = set()

    while stack:
        top = stack[-1]

        if not top in seen:
            while top.left:
                seen.add(top)
                if top.left:
                    stack.append(top.left)
                    top = stack[-1]
                    seen.add(top)
                else:
                    break
    
        currentNode = stack.pop()
        inorder.append(currentNode.val)

        if currentNode.right:
            stack.append(currentNode.right)
        
    return inorder

def itInorderClean(root):
    stack = []
    result = []
    current = root

    while current or stack:
        # go as far left as possible
        while current:
            stack.append(current)
            current = current.left
        
        # process node
        current = stack.pop()
        result.append(current.val)
        
        # move to right subtree
        current = current.right
    
    return result