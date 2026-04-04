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
                if top.left:
                    stack.append(top.left)
                    top = stack[-1]
                    seen.add(top)
                else:
                    break
            seen.add(top)
        
        currentNode = stack.pop()
        inorder.append(currentNode.val)

        if currentNode.right:
            stack.append(currentNode.right)
        
    return inorder