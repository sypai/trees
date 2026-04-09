def construct(nums):
    size = len(nums)
    if size == 0:
        return None
    mid = size // 2
    root = TreeNode(nums[mid])

    root.left = construct(nums[:mid])
    root.right = construct(nums[mid+1:])

    return root