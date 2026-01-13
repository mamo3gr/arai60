import timeit
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# インデックス計算
class SolutionIndexCalc:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes = [root]
        results = []
        left_to_right = True
        while nodes:
            values = [0] * len(nodes)
            next_level = []
            for i, node in enumerate(nodes):
                value_i = i if left_to_right else -1 - i
                values[value_i] = node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            results.append(values)
            nodes = next_level
            left_to_right = not left_to_right
        return results


# 2回走査（値は内包表記、ノードは通常のループ）+ reverse()
class SolutionTwoPass:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes = [root]
        results = []
        left_to_right = True
        while nodes:
            vals = [n.val for n in nodes]
            if not left_to_right:
                vals.reverse()
            results.append(vals)
            next_level = []
            for n in nodes:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            nodes = next_level
            left_to_right = not left_to_right
        return results


# 2回走査（すべて内包表記）
class SolutionComprehension:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes = [root]
        results = []
        left_to_right = True
        while nodes:
            vals = [n.val for n in nodes]
            if not left_to_right:
                vals.reverse()
            results.append(vals)
            nodes = [child for n in nodes for child in (n.left, n.right) if child]
            left_to_right = not left_to_right
        return results


# 1回走査（すべて手動ループで append）
class SolutionOnePass:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes = [root]
        results = []
        left_to_right = True
        while nodes:
            vals = []
            next_level = []
            for n in nodes:
                vals.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            if not left_to_right:
                vals.reverse()
            results.append(vals)
            nodes = next_level
            left_to_right = not left_to_right
        return results


def build_complete_tree(depth):
    if depth == 0:
        return None
    root = TreeNode(0)
    queue = deque([root])
    for i in range(1, 2 ** (depth - 1)):
        node = queue.popleft()
        node.left = TreeNode(i)
        node.right = TreeNode(i + 1)
        queue.append(node.left)
        queue.append(node.right)
    return root


def run_benchmark():
    depths = [12, 15, 17]
    iterations = 100

    solutions = [
        ("IndexCalc", SolutionIndexCalc()),
        ("TwoPass", SolutionTwoPass()),
        ("Comprehension", SolutionComprehension()),
        ("OnePass", SolutionOnePass()),
    ]

    header = f"{'Nodes':>10} | " + " | ".join([f"{name:13}" for name, _ in solutions])
    print(header)
    print("-" * len(header))

    for d in depths:
        root = build_complete_tree(d)
        total_nodes = 2**d - 1
        results = []
        for name, sol in solutions:
            t = timeit.timeit(lambda: sol.zigzagLevelOrder(root), number=iterations)
            results.append(f"{t:13.4f}")

        print(f"{total_nodes:10,d} | " + " | ".join(results))


if __name__ == "__main__":
    run_benchmark()
