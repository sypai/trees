def find_left_most_child_of_right_child(node):
    curr = node.right
    while curr.left is not None:
        curr = curr.left
    return curr

def first_ancestor_which_is_left_child(node):
    curr = node
    while curr.parent is not None:
        if curr == curr.parent.left:
            return curr.parent
        curr = curr.parent
    return None

def find_successor(root, node):
    if root is None or node is None:
        return None
     
    if node.right:
        return find_left_most_child_of_right_child(node)
    else:
        return first_ancestor_which_is_left_child(node)
