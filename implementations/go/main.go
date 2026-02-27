package main

import "fmt"

func preorder(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Println(root.Val)
	preorder(root.Left)
	preorder(root.Right)
}

func main() {
	root := &TreeNode{Val: 5}
	root.Left = &TreeNode{Val: 3}
	root.Right = &TreeNode{Val: 7}
	preorder(root)
}
