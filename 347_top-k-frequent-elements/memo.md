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

## step 2

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/pull/15/files

`defaultdict` なるほどー。引数 `default_factory` に、キーが存在しなかったときのファクトリを登録できる。  
https://docs.python.org/3.11/library/collections.html#collections.defaultdict

高頻度なk個にだけ興味があるので、全体をソートせずに優先度付きキューが使える。  
O(log k) の操作をm回することになる。つまり O(m log k).

バケットソートを使うこともできる。時間計算量はO(n).  
実装してみたら実際のランタイムはそれほど速くなかった。
mやkが小さいと組み込みのソートや優先度付きキューの方が速いということか。

https://github.com/docto-rin/leetcode/pull/9/files

クイックセレクトというアルゴリズムもあるらしい。

### コメント集

https://discord.com/channels/1084280443945353267/1235829049511903273/1245555256360697949

>出題者の意図的には、dict の初期化をして数え、その後 list にして sorted に key function を渡して k 個取る、くらいが想定されているように見えます。  
>Counter を使うと、さすがに Counter の内部実装を書いて欲しいといわれるものと思います。
>
>で、そこから Quick select に手を出すのもいいですが、Python で書いても Native 実行の sorted に速度でおそらく劣り、(log はなかなか定数倍に追いつかない)またコードも複雑なので選択しないです。
>
>あとは、priority_queue ですね。
>
>つまり、私はこの PR に対しての感想は、実装方法の候補を十分に出して、その良し悪しを考えるということができていない可能性が高いが、入出力の一致したコードが書けて満足しているかもしれないので、見えているかを問うてみようというものです。

「実装方法の候補を十分に出して、その良し悪しを考える」を意識してこう。

https://discord.com/channels/1084280443945353267/1183683738635346001/1185972070165782688

>Top K を見つけるには、priority_queue に放り込むのでもいいですが、計算量としてソートしているのと変わらないですね。

>書くと大変ですね、っていいましたが、やっぱり、Quick Sort は聞かれても不思議はないので、Quick Select も常識範囲だと思います。

https://discord.com/channels/1084280443945353267/1227073733844406343/1231268645628416020

>常に Top K Frequency をモニタリングし続けるというストリーミングアルゴリズムとして解くことも可能ではないか

これは思ったけど大変そうなので避けてた。平衡木を使うとできるらしい

https://discord.com/channels/1084280443945353267/1367399154200088626/1371325723612151918

>実際の仕事のときを少し想像して欲しいんですね。
>
>あなたは、配属されたチームでとりあえずセットアップができた。テックリードはめちゃくちゃ忙しそうです。
ウェブページになんかの上位 K 件を表示する機能をつけたいが、テックリードがやると別に書くのはすぐだがレビューアーとやりとりをしてプロダクションに持っていってとすると大変だ。
>
>代わりに引き取ってあげたい。みたいなのが状況です。
>
>同率になることはいまのところありえない。としても、事情が変わるかもしれないので、同率 K 位がたくさんあると全部出ますは避けたほうが良いように思いますね。

これとても大事だ。

https://github.com/fuga-98/arai60/pull/10#discussion_r1967591652

`sorted` の `key` に `dict.get` を渡すと、valueだけ返ってくるんだ。へえー。

## step 3

- `Counter` の中身を聞かれる想定で、同じ挙動をベタに実装する
- 高頻度上位を取るには、(1) 組み込みのソート、(2) 優先度付きキュー、(3) バケットソート、のうちから (1) を選ぶ。コードの簡潔さとそこそこの速度が理由

## TODO

- [ ] クイックセレクトの調査
- [ ] クイックソートの復習
- [ ] 平衡二分探索木の復習

