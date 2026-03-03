## step 1

文字列 `s` と、列数 `numRows` が与えられたとき、`s` のzigzag patternで変換したものを求める。
例えば `s = 'PAYPALISHIRING'` に対し `numRows = 4` のとき答えは `PINALSIGYAHRPI` になる。

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

制約としては  `1 <= len(s) <= 1000`, `1 <= numRows <= 1000`.
`s` に含まれる文字はアルファベットの小文字・大文字とカンマ・ピリオド。

単純に考えると、前述のようなグリッドに `s` を詰め直せば良さそう。
グリッドの列数を求めることを考えている最中に、2次元の、空白 = `None`のあるグリッドではなく、
`list[list[str]]` の各行に `s[i]` をappendしていけばいいことに気がつく。
zigzagの方向のうち、下降しているのか、斜め上に行っているのかをboolで持てば、
次にどの行に入れるかインデックスの計算ができる。

処理時間とメモリ使用量を見積もる。
時間計算量は `s` を一度舐めるだけなので `O(N)`. Pythonの処理能力を10^7 steps/sec とすると、
1000 / 10^7 = 0.1ミリ秒のオーダー。
空間計算量も `O(N)`. `s` をzigzagにトラバースした結果を `list[list[str]]` に詰める。

`numRows = 1` のときのインデックス処理に一度躓いた。
2以上のときは、次の行 `row` が更新されたあと、最下部や最上部に当たっていたら方向を変える、とするが、
1のときにはvalidな範囲を超えてしまう。いったん min, max で戻すことにするが、もう少しいい方法がありそう。

## step 2

ChatGPTにレビューしてもらいながらコードを整理する。
`numRows = 1` の場合は早期終了することで、進行方向を返るロジック（前述）がシンプルになる。
あと引数 `numRows` のsnake_caseでの置き直しを止めた。

### 他の人のコード

#### https://github.com/Satorien/LeetCode/pull/59

下降している、かつ境界を超えていたら、方向を変えてインデックスを修正してcontinue, というのができる (step1).
そのループではカウンタを進めない。

行ごとに都度joinしたstrを持つ (step2), というパターンもあるが、strがimmutableなので都度生成することになる。
メリットは `list.extend()` がなくなり僅かに可読性が上がる。

方向をboolではなく1, -1で持つパターン (step3).

#### https://github.com/naoto-iwase/leetcode/pull/61

二重のwhileループ (step1). 底を打つまで下降、先頭に戻るまで上昇、という動きが分かりやすい。

`rows`, `row` とあったとき、後者は `rows` の要素なのかインデックスなのか分かりづらい (step3).

#### https://github.com/shintaro1993/arai60/pull/64

周期性から `row_index` を求められるっぽい。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.6oum2lb2o7j4

#### https://github.com/saagchicken/coding_practice/pull/22/changes/BASE..bfa74b398f6e52de5fef3d930288b21029ae2d2d#r2009413184

`row_index` をGeneratorで送り込むアイデア。

#### https://github.com/saagchicken/coding_practice/pull/22#discussion_r2009416979

Generator expressionによる2重内包表記。目の左右の動きがきつい。

#### https://github.com/saagchicken/coding_practice/pull/22#discussion_r2009508424

>この問題、出題意図は、お手玉できるか、な気もします。
> 
>Generator は内部的には、ある種のコンテキストを持っていて、計算の続きに戻れるようにしています。だから、それなりに重いです。
> 
>そういうわけで、手続き型の手法で構造を組み合わせられるかが想定だろうなと思います。

#### https://github.com/olsen-blue/Arai60/pull/61#discussion_r2040670667

周期は `2 * (numRows - 1)` で、この周期ごとで `itertools.batched` を使って `s` をchunk単位にする。
chunk内は `row_index` の処理が比較的簡単。

## step 3

`direction` を決めてから `row_index` を更新する、という順番だとコードはすっきりする。
`list[list[str]]` に append, 最後にflattenしてstrにする、というのが分かりやすい。
2重内包表記は目が滑るのでfor文で展開する。
