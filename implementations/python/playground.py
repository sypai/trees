from implementations.python.tree_node import TreeNode
from patterns.traversals.preorder_dfs_iterative import dfs_preorder, dfs_preorder_deque
from patterns.traversals.preorder_dfs_recursive import preorder
from patterns.traversals.bfs import bfs
from problems.algoexpert.easy.node_depths import node_depths
from problems.algoexpert.medium.invert_bt import invert

def build_sample_tree():
    """
            A
           / \
          B   C
         / \   \ 
        D   E   F
    """
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")
    root.right.left = TreeNode("F")

    return root

def build_sample_tree_1():
    """
            1
            /\
            2 3
            /\ /\
           4 5 6 7
          /\
          8 9
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right =TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    return root

def inorder(node):
    if node is None: 
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


if __name__ == "__main__":
    root = build_sample_tree_1()
    # dfs_preorder_deque(root)
    # print("-=--")
    # preorder(root)
    # print("==========")
    # bfs(root)
    inorder(root)
    invert(root)
    inorder(root)