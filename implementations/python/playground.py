from implementations.python.tree_node import TreeNode
# from patterns.traversals.preorder_dfs_iterative import dfs_preorder, dfs_preorder_deque
from patterns.traversals.preorder_dfs_recursive import preorder
# from patterns.traversals.bfs import bfs
# from problems.algoexpert.easy.node_depths import node_depths
# from problems.algoexpert.medium.invert_bt import invert
from problems.algoexpert.medium.merge import merge

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

    # [3, 2, 5, 4, 9, 8, None, None, None, None, None, None, 7, 6, None, None, None, None]
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

def build_sample_tree_A():
    """
         1
        / \
       2   3
      /     \
     4      5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root


def build_sample_tree_B():
    """
         7
        / \
       8   11
      /\     \
     9  10    12
              /
            13
             \ 
             14
    """
    root = TreeNode(7)
    root.left = TreeNode(8)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(10)

    root.right = TreeNode(11)
    root.right.right = TreeNode(12)
    root.right.right.left = TreeNode(13)
    root.right.right.left.right = TreeNode(14)
    return root
    


def inorder(node):
    if node is None: 
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


if __name__ == "__main__":
    rootA = build_sample_tree_A()
    rootB = build_sample_tree_B()
    # dfs_preorder_deque(root)
    # print("-=--")
    # preorder(root)
    # print("==========")
    # bfs(root)
    # inorder(root)
    # invert(root)
    # inorder(root)
    root = merge(rootA, rootB)
    preorder(root)

    

