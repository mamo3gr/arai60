## step 1

与えられた数字の配列 (array) のうち、合計が `k` になる subarray の総数を調べる。  
brute-forceとして、すべての subarray を取り出すことを考えると `O(N^2)` の時間計算量がかかる。ここで `N` は配列の長さである。Constraintsより `N` は最大で 2 * 10^4 なので、10^6ステップ/秒かかるとすると400 秒. 確実にタイムアウトする。

Hintを見たら累積和を使うことが書かれていたのでやってみる。インデックスの扱いが煩雑。これでもまだ `O(N^2)` を抜けられない。

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = {0: 0}  # i -> sum(nums[:i-1])
        count = 0
        for i in range(len(nums)):
            cumulative_sum[i + 1] = cumulative_sum[i] + nums[i]

            for j in range(0, i + 1):
                # subarray = nums[j:i+1]
                total = cumulative_sum[i + 1] - cumulative_sum[j]
                if total == k:
                    count += 1

        return count
```

適当なSolutionを読んでみる。上記コードでいう `j` ループの部分が、key=累積和、value=出現回数のハッシュマップで置き換えられると理解した。  
書けた。工夫によって `O(N^2)` が `O(N)` に減るのに感動した。  
一方で読む側からしたら、この工夫が説明されないと何をやっているのかさっぱり分からなさそう。

- 累積和を使う
- 配列を舐めながら累積和を覚えておく
- ハッシュマップから、補数となる累積和の出現回数を引く
- いま計算した累積和でハッシュマップを更新する

という操作を一度にやるので煩雑。
