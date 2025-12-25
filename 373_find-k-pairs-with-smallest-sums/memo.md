## step 1

最もシンプルには、nums1とnums2からすべての組み合わせを取り出して和を計算し、ソートして小さい順にkペア取り出す。実装したがMemory Limit Exceeded.

```python
from itertools import product


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        pairs = [(n1, n2) for n1, n2 in product(nums1, nums2)]
        pairs_sorted = sorted(pairs, key=lambda x: x[0] + x[1])
        return pairs_sorted[:k]
```

すべての組み合わせを保持し続ける必要はなさそう。k個のmin-heapを持っておくのはどうか。

```python
from itertools import product
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        smallest_pairs = []
        heapq.heapify(smallest_pairs)

        for n1, n2 in product(nums1, nums2):
            node = (-1 * (n1 + n2), n1, n2)
            heapq.heappush(smallest_pairs, node)
            while len(smallest_pairs) > k:
                heapq.heappop(smallest_pairs)

        return [(n1, n2) for _, n1, n2 in reversed(smallest_pairs)]
```

Time Limit Exceeded. 手続きで工夫が必要そう。  
`nums1` も `nums2` も、後ろの方は考慮するまでもないケースが大半になりそう。

10分ほど考えて思いつかなかったので回答を見る（LeetCodeのEditorial）。
`nums1`, `nums2` のそれぞれの要素を指すインデックスを `(i1, i2)` として、`(0, 0)` は必ず答えに入る（なぜならば、どちらの配列もソート済みなので）。ここで、次に和が小さいペアは `(0+1, 0)` か `(0, 0+1)` である。この候補をmin-heapに入れて、先頭を取り出して繰り返せば良い。ただし、min-heapに入れる座標はすでに検討済みのペアもあるので、これはハッシュマップで重複を弾く。

答えに採用されたペアの周りを見るのかな、くらいまではいけたが、そこから手が出なかった。この辺をアルゴリズムにまで落とせるようになりたい。
