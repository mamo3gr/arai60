## step 1

二分木（の根）が与えられたとき、それが二分探索木 (BST: Binary Search Tree) であるかを判定する。ノードの最大数は10^4.  
おさらいしておくと、二分探索木では、任意の親ノードに対し、左のsubtreeに含まれる値はすべて親よりも小さい。右のsubtreeは同様にすべて大きい。  
左右のsubtreeいずれも二分探索木であることから、再帰が当てはまりそうに思う。あるノードからなるsubtreeが二分探索木であるとき、(1) その左右のsubtreeがやはり二分探索木で、(2) 左のsubtreeの最大値 < 親ノード、かつ (3) 親ノード < 右のsubtreeの最小値、を満たせば良さそう。つまり、再帰しながら、二分探索木であるかのboolとともにminとかmaxを返せば良さそうに見える。

ところで `root is None` なときはどちらなんだろうか。もはや木ですらないし、比較する値もないが…。  
→Geminiと議論したところ、空の木は二分探索木としてよいみたい。理屈としては、ノードがひとつだけの木を考えたとき、そのsubtreeも二分探索木なはずで、subtree=空の木だから。  
Web上の資料を探してもらったが、明確に定義としてそう書いてあるものは見つけられなかった。

処理時間とメモリ使用量を見積もっておく。  
処理時間については、ノード数を `N` とすると、すべてのノードを辿る必要があるので最悪 `O(N)`. ただし条件を満たさない箇所を見つけ次第終了できる（後で気がついたが、この早期終了はstep1では未実装だった）。ノードは最大10^4で、ノードあたり5ステップ、Pythonの実行時間を10^6 [steps/sec] と仮定すると、5 * 10^4 / 10^6 = 50ミリ秒のオーダーを予想する。  
メモリについては、線形リストになっている場合が最悪で `O(N)`. 答え・最小値・最大値でそれぞれ28 bytes として、28 * 10^4 = 280KBくらいのオーダーを予測する。

nodeがNoneな場合もチェックせずに再帰できるようにする。かつ、この場合は擬似的な無限大を返す。制約から `node.val` は [-2^31, 2^31-1]. `sys.maxsize` を使っても良いかもしれないが、64bit環境でないと前述の値域を超えられない。  
subtreeの最大値・最小値として、親のvalとも比較する必要があるバグを踏んだが、何とかテストはパスできた。

## step 2

再帰で書けるということは反復的にも書けるということだが、結構面倒そう。

### 他の人のコード

#### https://github.com/huyfififi/coding-challenges/pull/39

>各nodeが、左のnodeと右のnodeからそれぞれ報告書をもらって、上のnodeに (自分がBSTの条件を満たしているか, 自分からなる部分木の最小値, 部分木の最大値) を返せば良いと思った。

考え方は合ってたっぽい。

>Binary Search Tree を inorder traversal するとincreasing (sorted) sequence になる。

そうかー。[108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)でやってたじゃん。  
inorderでtraverseして、sortedかどうか調べたら良い (step1-4).

>In general, adding words like `is`, `has`, `can,` or `should` can make booleans more clear.

ヘルパー関数の命名。`is_valid` で始めると、`get_min_max` はどうすんねん、と思った。

再帰するときに、`lower_bound`, `upper_bound` を渡すというパターン (step1-2).  
iterativeに書くには、`(node, lower_bound, upper_bound)` をスタックに詰めていけば良い (step1-3).  
左をずっと掘って行って、下限を更新するパターン (step1-5).  
いろいろな書き方があるんだなあ。

#### https://github.com/plushn/SWE-Arai60/pull/28

ジェネレーター式 `yield` と、その移譲 `yield from` を使って、再帰してinorderにvalueを取り出すパターン。`itertools.pairwise()` で2つずつ値を取り出すことができ、昇順か調べている。

キューに `(node, minimum limit, maximum limit)` を詰めていくパターン (step3). 条件を満たさない箇所があったらすぐに終了するし、これが良さそう。

#### https://github.com/Kaichi-Irie/leetcode-python/pull/29

本筋ではないが、だいぶ `frontiers` が見慣れてきたので、自分でも使おうかな。

やはり `{lower,upper}_bound` を与えるパターンのほうがスッキリする。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.r5pdnx6retf4

>通りがけ inorder traversal をしながら、値が大きくなっていくかを確認、という方法もありますね。  
>これも書いてみるといいかもしれません。

https://github.com/nittoco/leetcode/pull/35/changes/BASE..cf57a354ba6d4fd06a3454283c3cec50011ce0c4#r1739978684

>Generator + 再帰、強力ですね。pros cons の cons としては、再帰の深さの限界があること、走りかけの Generator を木の深さ分だけ作るのでそこそこ重いことがありそうですね。

書けるが進んでやるものでもないみたい。

https://github.com/olsen-blue/Arai60/pull/28#discussion_r1948252913

>上から範囲の制約を下げていくか、下から値の範囲を上げていくか、インオーダーで出力して昇順になっているか、などでしょうか。

自分だけではここまでの幅が出せなかった。うーむ。  
せっかくだからそれぞれ書いてみよう。

in-order traversalによる解法がまだ理解できていない。ちょっと頭の中で寝かせる。  
コメント集を漁り直して、分かりやすい実装を見つけた。  

https://github.com/YukiMichishita/LeetCode/pull/8/changes#diff-4715b26790b92230b162cee20ac77591864a09b081158d7e9d0def2dc4ce5dc7R40-R81

左に掘れるだけ掘る（スタックに積みながら）、popして値をチェック、右があるなら右に行く。  
in-order traversalをそのまま説明していただけか。  
書いてみる。「左に掘れるだけ掘る」をinner functionに括りだすと分かりやすかった。  
左を掘ってないrootをスタックに積むと、それをpopした後の処理が、一般のノードの処理と異なるのが辛い（が、関数への括り出しによってwhileループ前に掘りやすくなる）。

他に、「左掘り尽くした？」フラグとノードとのタプルを積むパターン。  
https://github.com/naoto-iwase/leetcode/pull/33/changes/BASE..2404c21c24a749b6f871d9030b7df0096beb856d#r2504847397

#### bottom-up, iterative

あとはbottom-upもパターンとしてある。以下を参考にする。  
https://github.com/naoto-iwase/leetcode/pull/33/changes/BASE..2404c21c24a749b6f871d9030b7df0096beb856d#r2479195403

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [([], root, [], [])]
        while stack:
            from_to, node, left, right = stack[-1]
            if not left and node.left:
                stack.append((left, node.left, [], []))
                continue
            if not right and node.right:
                stack.append((right, node.right, [], []))
                continue
            if left and left[1] >= node.val:
                return False
            if right and node.val >= right[0]:
                return False
            r = left + [node.val] + right
            from_to += [min(r), max(r)]
            stack.pop()
        return True
```

結構読むのが難しかった。  
スタックに積んでいるのは、部分木のmin-max, 部分木のルートノード、左の部分木のmin-max, 右の部分木のmin-max. `from_to`, `left`, `right` という命名が分かりにくい。  
トラバースの順序は後順走査 (post-order traversal) に近い。左の部分木→右の部分木→自分の順。自分以下の部分木のmix-maxを`from_to`に詰めて、親に返す。親は`left`, `right` でそれを受け取る。  
手なりでやると自分が最初にスタックから取り出されてしまうので、まずはpopせずに `stack[-1]` で参照する。未処理の左があるならスタックに積んでcontinue（右も同様）。  
左右が処理済みなら、`left_max < node.val < right_min` を満たしているかチェックし、自分を根とした部分木のmin-maxを`from_to`に更新する。ここまで完了したら、はじめてpopする。  
ここまで読み解いて、何が分かりにくいかを言語化しておく。

* `from_to`, `left`, `right` から、何を引き継ぐのかイメージしにくい
* 走査順が分かりにくい。特に、葉ノードに突き当たったときの処理が明に書いてないので、ボトムから上がっていくイメージをしにくい。実際には4つのif文に引っかからず、`from_to = [node.val, node.val]` を親に上げる

左右の部分木について、「ある・ない」と「処理済み・未処理」の2軸あるのが面倒なんだな。  
愚直に書き下すのが自分としては分かりやすかった。

* スタックからいきなりpopしない（参照するだけ）、というのが自分には不自然に感じられたので、ひとまずpopして必要であれば積むようにした
  * もちろんオーバーヘッドがあるが、おどろきの低減を重視した
* 処理済みかどうかは、key=部分木の根ノード、value=Bound(min, max) とする辞書で管理することにした
  * スタックの積み方を適切にやれば `from_to` でmin-maxを引き継ぐことは可能だろうが、Pythonではややトリッキーに思われた
  * 追加のメモリ使用や、辞書を操作する時間のオーバーヘッドは許容する

## step 3

いろいろ書いてみたが、top-down, iterativeがしっくり来た。とてもシンプルに感じる。

