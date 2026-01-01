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

## step 2

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/pull/21

>二重ループを一重ループにしたいのでそのためにループ間で何の情報を保持したら良いかを考える.  

「引き継ぎ」の考え方に近い。このコーディング練習会のひとつの大きなテーマだ。

>iから始まるsubarrayで, `sum(nums[j:i])`の値がkになるjを探していると理解する.  
>累積和（ヒントを見た）を使うと, sum(nums[j:i]) = cumsum[i] - cumsum[j]になる. iを用いてjを特定するには, i, kが与えられているときにcumsum[j] = cumsum[i] - kとなるjを探す問題になる

これがノーヒントで思いつければなあ。

https://github.com/komdoroid/arai60/pull/6

累積和は `prefix_sum`, `running_total` ともいう。

https://github.com/Kaichi-Irie/leetcode-python/pull/26

正の数のみが含まれる場合はtwo pointersでもできる。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.bp0g0ai41eln

>現実的にはパフォーマンス不足がどういう感じになるかというと、たとえば、「一日一回深夜に30分で更新作業が走るようにしておく」などしてあるパイプラインが、だんだんデータとともに伸びていって「朝になっても更新が終わらないなあ」みたいになってきます。あるいは「3日に1回くらいメモリー不足で更新プログラムが落ちる」みたいになってきます。
>
>そうすると、手戻りが発生して、どこで問題が起きているかを漁ることになります。そして、見つけたら修正です。
だいたい、はじめにいわれたときの要件を守らない使われ方が気が付かないうちにされていて、だんだん耐えられなくなって崩壊するわけですね。
>
>今回のこのコードは、想定される実行時間がそれほど長くなく、またメモリーも終了したら開放されるので、変なリスクをわざわざ取らないで単純で読みやすいほうに寄せたくなります。上のような事象を引き起こす可能性がとても小さそうだからです。

すごく現実味のある現象の説明。

## step 3

いまの `n in nums` に対する累積和 `prefix_sum` と、`prefix_sum_to_count` とが混在するのがちょっと混乱のもとかも。

