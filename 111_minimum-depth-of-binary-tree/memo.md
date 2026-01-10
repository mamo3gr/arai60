## step 1

与えられた二分木に対し、最小の深さを求める。  
子を持たないノード＝葉ノードのうち、最小の深さを求めれば良い。ちなみに深さ＝rootノードからのノード数（rootノードと自身を含む）。  
幅優先と深さ優先の2通りが考えられるが、浅いところで葉ノードを見つけたら終了できる幅優先の方が優れていそう。

ノードの数を `N` とすると、時間計算量は `O(N)`. 空間計算量も `O(N)`.  
ノードは最大10^5なので、時間は log10^5 / 10^6 [steps/sec] = 1.67 x 10^(-5) 秒 = 0.167 マイクロ秒で、マイクロ秒オーダーで処理できそう。  
メモリは同様に log10^5 * 8 bytes = 132 bytes.

## step 2

深さ優先探索を再帰でも書いてみる。

途中でimplicit falseの使い分けに自信が無くなったので、スタイルガイドを読み直す。  
https://google.github.io/styleguide/pyguide.html#214-truefalse-evaluations

>Always use if foo is None: (or is not None) to check for a None value.

`None` チェック時には `is None` にする。implicit falseによる判定だと、`None` であるかを確かめたいのに `False` や 0, 空のリストであっても引っかかってしまうから、だと想像する。

### 他の人のコード

#### https://github.com/Shoichifunyu/shofun/pull/16

再帰での実装。ノードごとの分岐を葉ノード・子ノード1つ・子ノード2つの場合にしている（子ノード1つの場合をexplicitに書いている）。結局どちらかのminを返せばいいので、個人的にはこの分岐は不要に思う。

#### https://github.com/plushn/SWE-Arai60/pull/22

キューを用いた幅優先探索。現在の深さのノードとそれらの子ノードを同じキューに入れ、現在の深さのノード=調べるノード数を保持する（したがって深さごとの探索が区切れる）。こんな書き方もできるのか。コメントされていたが、タプルにして深さを持つ方が素直そう。

#### https://github.com/docto-rin/leetcode/pull/21

再帰での分岐について、もうちょっと幅を見つけた。

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

葉ノード、左だけ、右だけ、左右と、MECEに並べるのも分かりやすいかも。この場合は、MECEだよという意図を示すために、`elif` を続けるのが好みだ。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.prowafrzksyh

>左右のノードは配列に入れてループで回す手がある。

処理上では左右を区別する必要は無いので、コードも減るしタイプミスによるバグも防げるし、これは良い。

>この depth の更新は whileの一番下のほうが素直じゃないでしょうか。（つまり、nodes_depth の更新とともに数を増やします。）

depthを更新するタイミングの自然さに気を配る。入出力が合うかのガチャをやり始めると意識が離れてしまう。

### 補題

再帰を使うメリット・デメリットをおさらいしてみる。個人的には、関数の中で同じ関数を呼ぶというのがたまにこんがらなるので避けがちになっている。Geminiと壁打ちしつつ整理する。

**メリット**

- 分割統治法で解ける問題や木構造のデータが、分かりやすくコードに落とし込める
- 状態管理をスタックに任せられる（ある状態を引数として再帰するので）。キューを使うと、それら状態（本問でいう現在の深さとか）を自分で管理する必要がある

**デメリット**

- スタックオーバーフローのリスクがある
  - Pythonでは再帰の上限数が決まっている（通常は1000）。これに到達すると `RecursionError` が発生する
    - `sys.getrecursionlimit()` で調べたところ本問題では 550000 だった
  - （Pythonは非サポートだが）言語によっては、再帰がループに自動変換される（末尾再帰の最適化）
- 呼び出しコストのオーバーヘッドがある

まとめると、問題やデータの構造にバッチリ当てはまるなら再帰を使えばいいし、そうでないならやめればよい。使う場合は、再帰の深さが上限に引っかからないか確認が必要。

## step 3

自分ならキューを使う実装の方が好みかなー。

