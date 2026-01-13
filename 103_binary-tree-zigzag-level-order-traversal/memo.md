## step 1

与えられた二分木に対し、zig-zag order - つまり左→右、右→左、… の順でトラバースした結果（値）を返す。  
これ実務上はどんな応用があるのかな。→Geminiに聞いてみたが納得できる答えは得られなかった。

「いまどっち向きか？」を記憶しながら、上（根）からiterativeにキューに詰めていけば良い。積むときは末尾にappendして、popを先頭から・末尾からやる。dequeが良さそう。反対に、詰める時点で先頭・末尾に振り分けることもできそうだけど自分には不自然に思える。

時間計算量・空間計算量の議論は[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)と同様。同問を解いた https://github.com/mamo3gr/arai60/pull/25 を参照のこと。

前問のように、for each nodeで `val` の取得と子ノードのappendをやると、順番がこんがらがる。  
値は逆順でリストアップしたいが、子ノードは正順でappendしたい。どちらかだけを後でreverseするか、2回に分けてやるか。2重に走査するオーバーヘッドがあるが、後者のほうが分かりやすそう。

## step 2

再帰でも書いてみた。試しにノードを逆順で走査して処理してみたが、いたるところに `if reverse` が出てきて気持ち悪い。気を使うポイントが多すぎてstep 3で一発で通る気がしない。

### 他の人のコード

#### https://github.com/plushn/SWE-Arai60/pull/27

先に `values` (for a level) の配列を用意しておいて、逆順なら後ろから詰める (step2).

やっぱり値だけ後からreverseするのがいい。値と子ノードの列挙をinner functionで括りだすと見通しが良い。`list.reverse()` なるメソッドがある。  
https://github.com/plushn/SWE-Arai60/pull/27/changes#r2651201614

reversedはiteratorを返す。  
https://docs.python.org/3/library/functions.html#reversed

`sequence.reverse()` はin-placeに逆順にする。  
https://docs.python.org/3/library/stdtypes.html#sequence.reverse

メモリ確保の効率性からもこっちのほうが良さそう。

>This method maintains economy of space when reversing a large sequence.

#### https://github.com/naoto-iwase/leetcode/pull/31

zigzag or notを変数で持つのではなく、levelの偶奇から判定する (step1). この実装ではlevelを変数として持っているが、最終的なlist of listのlenからも取得できそう。  
個人的にはフラグの方がシンプルで良さそうに見える。

valuesを後で逆順にする以外の方法として、逆順 (`-1-i`) で配列にアクセスする、というのがある。Pythonの時点で速さを気にするか？というところはあるが、どちらかといえばこちらのほうが速いはず。

#### https://github.com/nanae772/leetcode-arai60/pull/27

Noneチェックせずに入れちゃって、valueをリストアップするときにチェックする、というパターンもある。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg に見つからず。前問 (102. Binary Tree Level Order Traversal) と同様ということだろうか。

### パフォーマンス比較

そもそもPythonを使っている時点でそこまで気にしてもしょうがないだろうが、Geminiにコードを吐かせてどれくらいの差なのか見てみる。  
環境は Python 3.14.2 [Clang 17.0.0 (clang-1700.4.4.1)] on darwin.

#### 値のリストアップ

* Index: 長さを確保したlistに対し、正順なら`i`, 逆順なら `-1-i` で値を入れる
* Reversed: listに正順・内包表記でappendした後、`list(reversed(values))` で逆順にする
* In-place: listに正順・内包表記でappnedした後、`values.reverse()` で逆順にする

```
     Nodes |  Index (s) | Reversed (s) | In-place (s)
------------------------------------------------------
        10 |    0.00091 |      0.00051 |      0.00037
       100 |    0.00691 |      0.00248 |      0.00204
     1,000 |    0.04754 |      0.01352 |      0.01166
    10,000 |    0.42567 |      0.12267 |      0.10490
   100,000 |    4.33081 |      1.24868 |      0.99488
```

単純な操作の量だけを考えると `Index` が速そうだが、インデックスを毎回計算するのに対し、内包表記などでネイティブコードに行ける `Reversed` の方が速いみたい。  
さらに`list.reverse()` の方がわずかかに速い。これはイテレータを受け取ってからリスト化するよりも、オーバーヘッドがないためだと考えられる。

#### 全体

とはいえ、これが全体に占める割合も気にする必要がある。コード全体もベンチマークを取ってみる。

* IndexCalc: 正順なら`i`, 逆順なら `-1-i` で値を入れる
* TwoPass: 値のリストアップ（内包表記）、子ノードのappendで2回走査する
* Comprehension: 値も子ノードも、内包表記で列挙する
* OnePass: 一度の走査で値のリストアップと子ノードのappendを行う

```
     Nodes | IndexCalc     | TwoPass       | Comprehension | OnePass
--------------------------------------------------------------------------
     4,095 |        0.0312 |        0.0180 |        0.0294 |        0.0185
    32,767 |        0.2127 |        0.1369 |        0.2241 |        0.1394
   131,071 |        0.8167 |        0.5380 |        0.8813 |        0.5508
```

TwoPass, OnePassが比較的速い。  
Comprehensionが遅いのが意外だったが、Gemini曰く `(node.left, node.right)` というタプルの生成に時間がかかっているらしい。

結論として、内包表記などネイティブコードに行ける方が速いし、走査が2回になるくらいの無駄も跳ね返せる。

## step 3

2回走査するのがそれほど問題にならないことが分かったので、値の列挙と、子ノードの列挙を分けて書く。正順か逆順かはフラグで直接管理する。

