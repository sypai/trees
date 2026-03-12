from collections import deque


# In my mental model of queue, I am seeing the counter of a grocery store on the left
# Nodes enter from the left and leave from right
# that's why appendleft and pop
def bfs(node):
    if node is None:
        return
    queue = deque([node])

    while len(queue) > 0:
        curr = queue.pop()
        print(curr.val)

        if curr.left is not None:
            queue.appendleft(curr.left)
        if curr.right is not None:
            queue.appendleft(curr.right)


# But ChatGPT says, convention is the opposite
# enqueue append
# dequeue popleft
# looking at the counter on the left - towards the 0 index
def bfs_convention(node):
    if node is None:
        return []
    traversal = []
    queue = deque([node])

    while len(queue) > 0:
        curr = queue.popleft()
        traversal.append(curr.val)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return traversal