def splitBST(
    root: TreeNode | None, val: int
) -> tuple[TreeNode | None, TreeNode | None]:
    # 入力ノードを出力に含まず、新規に生成するなら
    # import copy
    # root = copy.deepcopy(root)
    # ただし、木の高さにかかわらず `O(N)` になってしまう

    small_tree_sentinel = TreeNode(val=-1)
    big_tree_sentinel = TreeNode(val=-1)

    small = small_tree_sentinel
    big = big_tree_sentinel
    node = root
    while node:
        if val < node.val:
            next_node = node.left
            node.left = None

            big.left = node
            big = node
        else:
            next_node = node.right
            node.right = None

            small.right = node
            small = node

        node = next_node

    return small_tree_sentinel.right, big_tree_sentinel.left
