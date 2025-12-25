## step 1

最もシンプルには、nums1とnums2からすべての組み合わせを取り出して和を計算し、ソートして小さい順にkペア取り出す。`len(nums1) = N`, `len(nums2) = M` とすると O(NM) の空間計算量が必要になり現実的ではない。ダメ元で実装してみたがMemory Limit Exceeded.

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

すべての組み合わせを保持し続ける必要はなさそう。k個のmin-heapを持っておく。ただし、こうしても、min-heap操作 O(log k) が N * M 回必要なので、やはり現実的な時間では終わらなさそう。

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

予想通りTime Limit Exceeded. 手続きで工夫が必要そう。  
`nums1` も `nums2` も、後ろの方は考慮するまでもないケースが大半になりそうだが…

10分ほど考えて思いつかなかったので回答を見る（LeetCodeのEditorial）。
`nums1`, `nums2` のそれぞれの要素を指すインデックスを `(i1, i2)` として、`(0, 0)` は必ず答えに入る（なぜならば、どちらの配列もソート済みなので）。ここで、次に和が小さいペアは `(0+1, 0)` か `(0, 0+1)` である。この候補をmin-heapに入れて、先頭を取り出して繰り返せば良い。ただし、min-heapに入れる座標はすでに検討済みのペアもあるので、これはハッシュマップで重複を弾く。

答えに採用されたペアの周りを見るのかな、くらいまではいけたが、そこから手が出なかった。この辺をアルゴリズムにまで落とせるようになりたい。

## step 2

まずは自分なりに手直し。

- min-heapに入っているのはcandidatesだろうな。
  - これをnamedtupleとかdataclassにすることも考えたが、コメントで補うくらいでちょうど良さそう

あとは、あまり思いつかなかった。

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/pull/16#r2602118324

>アルゴリズムを実装する前に、まず時間計算量を求め、その計算量から実行時間を概算する

C++で約 1～10 億ステップ/秒、Pythonは約 100 万～1000 万ステップ/秒。

https://github.com/Yuto729/LeetCode_arai60/blob/3e2f2d5850d9ea9bf5244acdf0176a05de4e7b0c/find-k-pairs-with-smallest-sums/main.md

>nums1の最初のk行だけpushしておくと, (i,j)に対して(i,j+1)を探索すれば良くなるので重複することがなくなる.
>
>別のやり方として,(i+1, j) は j == 0 のときだけpushするというやり方がある. こうすることで, (i, j)(j != 0)は(i, j-1)からの遷移に限定されるので重複を防げる.

へえーなるほど。

heapへのpushを関数に切り出すのは良さそう。

https://github.com/yas-2023/leetcode_arai60/blob/bd4e251ca44d2eeea749b23505f3f4a4d08e711e/373/step3.py

`row_index`, `column_index` なるほど。どっちが列でどっちが行なのか混乱しそうなので、自分なら `i`, `j` とか `i1`, `i2` とかかな。

https://github.com/docto-rin/leetcode/blob/4065999a894a024ae5e65b34ad59fa30db9feb4d/0373-find-k-pairs-with-smallest-sums/0373-find-k-pairs-with-smallest-sums.md

解法にたどり着いているの素晴らしい。

### コメント集

https://discord.com/channels/1084280443945353267/1235829049511903273/1246118347863621652

yield generatorを使った実装。たしか遅いはずだし、可読性も比較的低そう。採用可能性は低いが選択肢として持っておけ、ということなのだろう。

