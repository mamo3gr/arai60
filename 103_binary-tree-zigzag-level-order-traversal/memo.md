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

