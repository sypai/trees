"""Find Nodes at Distance k from target"""
from collections import deque

def getParentMap(root):
    parentMap = {}

    def dfs(root, parent):
        if not root:
            return 
        
        parentMap[root.val] = parent
    
        dfs(root.left, root)
        dfs(root.right, root)

    dfs(root, None)
    return parentMap

def findNodesAtDistanceFrom(target, k, parentMap):
    
    seen = set()
    q = deque([(target, 0)])
    result = []

    while q:
        currentNode, distance = q.popleft()
        if currentNode in seen:
            continue
        seen.add(currentNode)

        if distance == k:
            result.append(currentNode.val)
        
        
        if currentNode.left:
            q.append((currentNode.left, distance + 1))
        if currentNode.right:
            q.append((currentNode.right, distance + 1))
        if parentMap[currentNode.val]:
            q.append((parentMap[currentNode.val], distance + 1))
        
    return result


def nodesDistanceK(root, target, k):
    if root is None:
        return []
    
    q = deque([root])
    parentMap = getParentMap(root)

    while q:
        currentNode = q.popleft()  

        if currentNode.val == target:
            return findNodesAtDistanceFrom(currentNode, k, parentMap)
        
        if currentNode.left:
            q.append(currentNode.left)
        if currentNode.right:
            q.append(currentNode.right)
        
    return []

