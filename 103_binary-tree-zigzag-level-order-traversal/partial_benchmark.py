import timeit


class MockNode:
    def __init__(self, val):
        self.val = val


# インデックス計算で直接逆順に詰める
def method_index_calc(nodes, left_to_right):
    values = [0] * len(nodes)
    for i, node in enumerate(nodes):
        value_i = i if left_to_right else -1 - i
        values[value_i] = node.val
    return values


# 正順で詰めてから reversed() してリスト化
def method_reversed_call(nodes, left_to_right):
    values = [node.val for node in nodes]
    if not left_to_right:
        return list(reversed(values))
    return values


# 正順で詰めてから list.reverse() (破壊的変更)
def method_inplace_reverse(nodes, left_to_right):
    values = [node.val for node in nodes]
    if not left_to_right:
        values.reverse()
    return values


def run_benchmark():
    sizes = [10, 100, 1000, 10000, 100000]
    iterations = 1000

    print(f"Fixed Iterations: {iterations}")
    print(
        f"{'Nodes':>10} | {'Index (s)':>10} | {'Reversed (s)':>12} | {'In-place (s)':>12}"
    )
    print("-" * 65)

    for size in sizes:
        nodes = [MockNode(i) for i in range(size)]

        t1 = timeit.timeit(lambda: method_index_calc(nodes, False), number=iterations)
        t2 = timeit.timeit(
            lambda: method_reversed_call(nodes, False), number=iterations
        )
        t3 = timeit.timeit(
            lambda: method_inplace_reverse(nodes, False), number=iterations
        )

        print(f"{size:10,d} | {t1:10.5f} | {t2:12.5f} | {t3:12.5f}")


if __name__ == "__main__":
    run_benchmark()
