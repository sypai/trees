from collections import deque

def node_depths(node):
    if node is None:
        return 0

    queue = deque([(node, 0)])
    depths = 0

    while queue:
        current_node, depth = queue.popleft()
        depths += depth

        if current_node.left:
            queue.append((current_node.left, depth + 1))

        if current_node.right:
            queue.append((current_node.right, depth + 1))

    return depths

def node_depths(node, depth):
    if node is None:
        return 0
    return depth + node_depths(node.left, depth+1) + node_depths(node.right, depth+1)
    