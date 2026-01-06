"""deppcopyが参照先のオブジェクトまでコピーしてくれるのか調べるコード"""

import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verify_deepcopy():
    parent = TreeNode(left=TreeNode(), right=TreeNode())
    copied = copy.deepcopy(parent)

    pairs = (
        (parent, copied),
        (parent.left, copied.left),
        (parent.right, copied.right),
    )
    for a, b in pairs:
        assert id(a) != id(b)


if __name__ == "__main__":
    verify_deepcopy()
