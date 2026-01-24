## step 1

`i`日目の株価をそれぞれ格納した配列 `prices` が与えられ、買う日と売る日を選んだとき、最大の利益を求める。  
単純に配列のminとmaxを駄目で、`min_i < max_i` を満たす必要がある。つまり、買う日は売る日よりも先でないといけない。

テストケースで手作業でやってみる。まず小さい値を見つけて、その後ろにある大きな値を探す。  
これは短い配列で人間の目の動きが速いからできるざっくり解法なので、もう少しプログラムに落とせる形にする。
配列を先頭から見て、今までのminを覚えつつ、いま入ってきた `prices[i]` が過去のmax profitよりも高くなるかを調べれば良さそう。
再帰でも書けそうだが、反復的に書いたほうが自然に思える。

計算量を見積もる。  
時間計算量は、配列を一度舐めるだけなので `O(N)` .
制約から `prices` の最長は10^5で、Pythonの処理能力を10^7 steps/sec とすると、
10^5 / 10^7 = 10msくらいのオーダーを予想する。
空間計算量は、`O(1)`. ここまでのminとmax profitをそれぞれ記憶すれば良い。

## step 2

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/37

minを更新するときはmax profitを更新する必要はない（その日に売ってもmaxにはならない）。

#### https://github.com/naoto-iwase/leetcode/pull/42

> `prices[1:]` はリストのスライスを新規作成するので、微小ながら無駄なメモリを使います。インデックスで 1 から回すか、`math.inf` 初期化で全要素を一度に処理するとより素直です。

なるほど。そこまで気にするほどでもないが、Pythonのスライス不便だな。

>- > 本質的には、
> - scanl min でその日までの最安の値。
> - zipWith (-) で利益。
> - max を取る。

この記法なんだろう。→Haskellらしい。

`itertools.accumulate` を使うとそれらしく書ける。  
https://docs.python.org/3.13/library/itertools.html#itertools.accumulate  
デフォルトはsumだけど、functionを渡せる。

`itertools.islice` を使っている。  
https://docs.python.org/3.13/library/itertools.html#itertools.islice  
これならコピーをせずにスライスを参照できるっぽい（以下の実装を読むあたり）。  
https://github.com/python/cpython/blob/v3.13.11/Modules/itertoolsmodule.c#L1795-L1832

#### https://github.com/nanae772/leetcode-arai60/pull/36

>`price < min_price`のときに場合分けをしたほうがよいのではないかという指摘。  
>自分はifのネストが増えるのが嫌でmax, minだけで簡潔させたが意図としてはif分岐の方が分かりやすいだろうか？

自分もmax, minの方が簡潔で好き。

>`min_price = prices[0]`と初期化しても`for price in prices[1:]:`とスライスしなくても動くという話。
>自分もそのようにしたが、prices[0]から始まってるのにまた0から回すのは自然では無い気もする。

これも分かる。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.8qw2um7il4s5

https://github.com/irohafternoon/LeetCode/pull/40#discussion_r2084763958

>この場合のループは、私の推測では30クロックかからないと思います。
>タイトなループの部分を見ると、
>prices[i] を取ってくる、引き算、max, min で回りますね。
>x86 では、LEA で取ってきて、SUB で引き算。max, min については CMOVcc という命令があって、CMP で比較した後のフラグで代入の有無を決められます。分岐予測もできそうです。
>よって、10命令以下で回りそうです。
>(ARM は CSEL があるようです。)

CPU命令までは自分は分からない。常識の範囲は広い。

### パフォーマンス測定

`min_price` を更新したときに profit を計算しないことと、関数呼び出しのオーバーヘッドから、ifが定数倍速い。  
Pythonを使っている時点で気にするほどの差でもなさそうだが。

```
--- 実行結果 (データ数: 100,000, 試行回数: 1000) ---
min/max:   5.6720 秒
if:        2.7700 秒
Itertools: 5.6882 秒
```

Python 3.14.2 (main, Dec  5 2025, 16:49:16) [Clang 17.0.0 (clang-1700.4.4.1)] on darwin.

## step 3

可読性の面でもそこまで悪くない気もしてきたので、ifを使って書いてやることにする。
配列が空のときはraiseする。自分なら、呼び出し元でチェックするし「空なら0を返す」ことを悪用されそう（仕様に対する必要以上の期待をされそう）なので。
`min_price` は `prices[0]` から始める。わざわざ `-math.inf` を使うのは過剰な気もするし、意味も通りそう。
