## step 1

`n` 行からなるテーブルに、一定の文法で文字（数字）を書いていくとき、`n` 行目の `k` 番目の文字を求める。
ここで文法とは、(1) 1行目は `0` を書く。(2) 次の行からは、前の行を変換する。`0` は `01` に、
`1` は `10` に。なお、特に注記がなければ `n` と `k` は 1-indexed である。

`n` は最大30で、`k` は最大 2^(n-1).
`n` 行目の文字数は 2^(n-1) になるから、文法通りに行を作って `k` 番目を返す、とすると
メモリも時間も足りなさそう。

方針を見つけるべく、適当な行数まで手作業で書き出してみる。

* 0
* 01
* 0110
* 01101001

木構造のようになっていることに気がつく。

```
           0
        /     \
      0        1
    /   \     /   \
  0     1     1     0
 / \   / \   / \   / \
0   1 1   0 1   0 0   1
```

例えば4行目の5番目（つまり `n` = 4, `k` = 5）を求めることを考える。
親は3行目の3番目。つまり `n - 1` 行目の `ceil(k / 2)` 番目である。
左右のどちらの子かは、奇数なら左、偶数なら右である。で、文法より、

* 親が `0` なら、左の子は `0`, 右の子は `1`
* 親が `1` なら、左の子は `1`, 右の子は `0`

である。

処理時間とメモリ使用量を見積もる。
時間計算量は `O(n)`.  最大で30行で、Pythonの処理能力を10^7 steps/sec とすると、
30 / 10^7 = 3マイクロ秒くらいのオーダーを予想する。
空間計算量は再帰あたり `O(1)` だが、再帰のスタックは `O(n)` 必要。
スタックフレームを150 bytesとすると、30 * 150 = 4.5 KB くらいのオーダーを予想する。

## step 2

GeminiとChatGPTにレビューしてもらいながらコードを整理する。指摘事項は以下。

* `ceil(k / 2)` は整数演算で書ける：`(k+1) // 2`
* 条件分岐が複雑で、排他的論理和（XOR）やビット反転で書ける
* 入力のバリデーションは一度だけやれば良い

ついでにwhileループ版も書いてみる。
結局ビット反転の回数を数えておいて、最後に根の `0` に作用すればよい。

### 他の人のコード

#### https://github.com/h1rosaka/arai60/pull/48

再帰、スタックとwhile, whileのみの実装。さらにシンプルな解法も。

`k-1` として0-indexedにすると、各層で右に行くかどうか＝親のsymbolが反転するかどうか、の回数が
`k-1` の1の個数と一致する。

2進数表記への変換には `bin()` が使える。  
https://docs.python.org/3.13/library/functions.html#bin  
3.10からは `int.bin_count` が使える。
https://docs.python.org/3.13/library/stdtypes.html#int.bit_count
`bin(self).count("1")` と同値、と書いてあるが、実装も一緒なんだろうか。
どうやら違うみたい。`bin_count` は30bitごとにカウントする。
https://github.com/python/cpython/blob/v3.13.12/Objects/longobject.c#L6253-L6254
clangあるいはGCCの場合は、x86のCPU命令を使う。
https://github.com/python/cpython/blob/v3.13.12/Include/internal/pycore_bitutils.h#L94-L95
そうでない場合は、SWAR (SIMD Within A Register) と呼ばれるアルゴリズムでカウントする。

https://github.com/h1rosaka/arai60/pull/48/changes#r2659245198

>(k + 1) // 2は切り上げ除算をしたいということだと思うので、意図を明確にするために(k + 2 - 1) // 2と書くのはありかと思いました。//を切り捨て除算の演算子として、(被除数 + 除数 - 1) // 除数で切り上げ除算になるという整数の離散性を使った公式ですね。

へええ。

#### https://github.com/garunitule/coding_practice/pull/46

https://github.com/garunitule/coding_practice/pull/46/changes#r2653431430

このassertもいいな。

```python
assert (k - 1).bit_length() <= n - 1
```

>n番目の行に対して前半部分は(n-1)番目の行を引き継いでいて後半部分はそれを反転させた行になっている

なるほど、こういう見方もあるのか。

#### https://github.com/Satorien/LeetCode/pull/46

garunituleさんと一緒で、前半なら前の行をそのまま、後半なら反転、という方針。
そのまま抜粋。こっちの方がわかりやすい。

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        previous_end = 2**(n-2)
        if k <= previous_end:
            return self.kthGrammar(n-1, k)
        return self.kthGrammar(n-1, k - previous_end) ^ 1
```

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.adit16u7jkla

https://discord.com/channels/1084280443945353267/1200089668901937312/1216054396161622078  
https://stackoverflow.com/questions/109023/count-the-number-of-set-bits-in-a-32-bit-integer#109025  
Hamming weight, popcount (population count), sideways additionとかいうらしい。
