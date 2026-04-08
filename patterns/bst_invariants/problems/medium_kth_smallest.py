def kthSmallest(root, k):
    if not root:
        return None
    
    stack = []
    counter = 1
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        if counter == k:
            return current.val
        
        counter += 1
        current = current.right
