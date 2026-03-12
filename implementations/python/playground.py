from implementations.python.tree_node import TreeNode
from patterns.traversals.preorder_dfs_iterative import dfs_preorder, dfs_preorder_deque
from patterns.traversals.preorder_dfs_recursive import preorder
from patterns.traversals.bfs import bfs


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


if __name__ == "__main__":
    root = build_sample_tree()
    dfs_preorder_deque(root)
    print("-=--")
    preorder(root)
    print("==========")
    bfs(root)