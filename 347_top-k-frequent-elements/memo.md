## step 1

頻度の高い順にk個、数字のリストを返す。順不同。

頻度を数えるのには `collections.Counter` が使えそう。  
https://docs.python.org/3.11/library/collections.html#collections.Counter

問題には関係ないが、3.7以降では、dictがそうであるように挿入順を覚えている。へえー

>Changed in version 3.7: As a dict subclass, Counter inherited the capability to remember insertion order.

問題にピッタリなメソッドもある。  
https://docs.python.org/3.11/library/collections.html#collections.Counter.most_common

`collections.Counter` はdictのサブクラスらしい。自分でも書けそう。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2frequency = dict()
        for n in nums:
            num2frequency[n] = num2frequency.get(n, 0) + 1

        number_and_frequencies_descending = sorted(
            num2frequency.items(), key=lambda x: x[1], reverse=True
        )
        return [n for n, _ in number_and_frequencies_descending[:k]]
```

時間計算量は O(n + m log m).

- ハッシュマップの更新O(1)をn個分。O(n)
- ユニークな数字の数をmとして、ソートにO(m log m)
- 最後に先頭kを取り出すのでO(k). ただしkはmよりも小さい

空間計算量は、O(m)

- ハッシュマップにO(m)
- 頻度順でソートした配列にO(m)

