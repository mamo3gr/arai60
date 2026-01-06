## step 1

新井さんの表の上では [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) と逆順で解いてしまった。別に問題ないとは思うが。

前問 (111.) と同様に解けそう。今度は最深まで調べる必要があるので、幅優先でも深さ優先でも速度上の差は無いように思える。  
時間計算量は最悪で `O(N)`（ただしノード数を `N` とする）。  
ノードは最大10^4なので、時間は log10^4 / 10^6 [steps/sec] = 1.67 x 10^(-6) 秒 = 1.67 マイクロ秒（くらいのオーダー）。
メモリは同様に最悪で `O(N)` 必要。具体的には log10^4 * 8 bytes = 13 bytes. これくらいのオーダー。

前問で再帰の書き方を試行錯誤したので、再帰のほうが自然に出てきた。  
テストをパスしてから気がついたが、子ノード（の片方）が `None` のケアができていなかった。`root is None` の場合は深さ0を返し、かつ `max` を取るので、結果的には問題無かった。

## step 2

こちらもキューを使って書いてみる。気にしたポイントは主に2つ。

- **左右の子ノードの調査：** 「存在する子ノード」に興味があるので、それを取り出す関数として括り出す。これでループのネストをひとつ減らせる。
- **深さの更新タイミング：** 次の深さのノードに行く際にしたい。これに伴って、一番外側のループは `while True` にして、途中でbreakするかチェックする。
  - 初期値を0にしてループの最初でインクリメントすると `while to_visit` にできるが、わずかにトリッキーに感じる

### 他の人のコード

#### https://github.com/Yuto729/LeetCode_arai60/pull/26

ノードと深さのタプルをスタックに入れる方式 (Step3). スタックから取り出す場合は、`max_depth` を更新して覚えておく必要がある。キューなら最後に取り出した `depth` が答えになるが、どちらにしろループの外側から束縛した方が可読性は高いだろう。

#### https://github.com/plushn/SWE-Arai60/pull/21

>Noneチェックですが、append前にやる方法のほか、pop直後にやる方法もあります。
>
>pop直後にやる方法について、prosはNoneチェックを現状のコードで3箇所あるのを1箇所に集約できる点、consは一時的にNoneがキューに入ることでループが多く回る点です。BFSにて幾何級数的に増加することがあるそうです。

`None` を気にせずキューに入れて、後で調べるパターンもある。

#### https://github.com/Shoichifunyu/shofun/pull/15

ノードと深さのタプルをdataclassで定義している。丁寧だが個人的にはちょっと過剰に思える。

#### https://github.com/docto-rin/leetcode/pull/20

>dequeを使った方が省メモリに実装できる

そうなんだ？

dequeの実装をちょっと読んでみる。ブロック単位の双方向連結リスト (Doubly linked list) になっている。ブロックの長さ `BLOCKLEN` は 64 と定義されている。

- https://github.com/python/cpython/blob/v3.13.11/Modules/_collectionsmodule.c#L201
  - https://github.com/python/cpython/blob/v3.13.11/Modules/_collectionsmodule.c#L129-L133

listはメモリ上の連続した領域を単にmallocしているように見える。

- https://github.com/python/cpython/blob/v3.13.11/Objects/listobject.c#L298

使用量という側面ではさほど差がないように見える。むしろdequeの方がオーバーヘッドがありそう。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.27jfjzhov3la

>あー、ちょっと全ノードに部下を立たせてみましょう。

マニュアル（＝関数）をノードに配るというイメージ。

再帰に行きがけと帰りがけがある。

## step 3

本問は再帰がしっくり来る。  
`None` な子ノードも再帰しても結果的には合うけど、ちゃんとチェックするほうが良さそう。

