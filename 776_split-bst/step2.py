def splitBST(root: TreeNode, val: int) -> tuple[TreeNode | None, TreeNode | None]:
    def helper(node: TreeNode | None) -> tuple[TreeNode | None, TreeNode | None]:
        if node is None:
            return None, None

        if node.val <= val:
            child_left, child_right = helper(node.right)
            node.right = child_left
            return node, child_right
        else:
            child_left, child_right = helper(node.left)
            node.left = child_right
            return child_left, node

    return helper(root)
