## step 1

2つの二分木が与えられ、それらをマージした木を返す。マージでは、重複するノードでは値 (`.val`) を合計する。片方のみノードがある場合はそれをそのまま使う。二分木に含まれるノードは最大で2000.  
再帰でも幅優先探索でも書けそう。パフォーマンスの観点から、時間・メモリの両面で大差は無さそう。幅優先探索だと、いま作っているノードに対し、接続先の（親の）ノードを覚えておく必要がありわずかに面倒。過去に整理した、再帰の「スタックに状態管理を任せられる」メリットが見えてきた。ということでまずは再帰で書いてみる。幅優先探索はStep 2でやる。

ここで、渡された二分木（のどちらか）を書き換えるか、新しい二分木を作るか？という幅が思い浮かぶ。特に破壊的になる理由も無いので、後者（新しい二分木を作る）。たぶんLeetCode的には渡された二分木を書き換えるほうが処理時間の点で優れているのだろうが、実務上、ユーザーとそうであることを約束しない限りは、破壊的な振る舞いは避けたほうが良いだろう。

処理時間について、それぞれの二分木に含まれるノードの数 `N1`, `N2` に対し、線形オーダーになる。というのも、ノードごとに必要な作業は (1) 各ノードから値を取り出す、(2) 新しいノードを作成する、(3) 子ノードを作成するために再帰する、くらいだから。メモリについても同様に、成果物として返す二分木を格納するのに、もとのノードに比例する領域が必要。  
制約から二分木あたり最大ノード数2000, 仮定としてノードあたり処理に5ステップ、Pythonの処理能力100万ステップ/秒を置くと、2000 * 5 / 10^6 = 0.01秒 = 10ミリ秒くらいのオーダーで処理できる算段。  
ノードあたり占有メモリを44bytes = 28bytes (int) + 8bytes * 2（左右の子ノードへのポインタ）とすると、新しく作成する二分木に対し44 * 2000 = 88 KBくらいのメモリが必要。実際にはもうちょっとオーバーヘッドがあるだろうが、オーダーとしてはこんなものだろう。

はじめに以下のように分岐をベタに書いたが、ノードがNoneでもval, left, rightを安全に（例外の発生なしに）取得するためのヘルパー関数を導入してみた。

```python
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        if root1 is not None and root2 is None:
            val = root1.val
            left = self.mergeTrees(root1.left, None)
            right = self.mergeTrees(root1.right, None)
            return TreeNode(val=val, left=left, right=right)
        elif root1 is None and root2 is not None:
            val = root2.val
            left = self.mergeTrees(None, root2.left)
            right = self.mergeTrees(None, root2.right)
            return TreeNode(val=val, left=left, right=right)
        else:
            val = root1.val + root2.val
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)
            return TreeNode(val=val, left=left, right=right)
```

## step 2

キューを使った実装もやってみる。step1では

>接続先の（親の）ノードを覚えておく必要があり

と書いたが、TreeNodeでは親を辿れないので、親（根）からキューに入れて、空の＝これから値をセットして欲しい子ノードをさらにキューへ入れていく、という流れになりそう。

### 他の人のコード

#### https://github.com/Shoichifunyu/shofun/pull/17

再帰による実装（「レビュー指摘後のリファクタ」）。root1とroot2を非対称に扱っているのが面白い。この変形は思いつかなかった。片方だけnon-Noneならばroot1がそうだと仮定していて、root1がNoneなら、root1とroot2をスワップして自身を呼び直している。

あまりに面白いので自分でも書いてみた。

#### https://github.com/plushn/SWE-Arai60/pull/23

dequeを使った実装 (step2). キューに詰めるタプルは、自分と同様に `(node1, node2, merged)`. ノードのマージ処理を関数として括り出していて、メインのループがかなりすっきりしている。ただし、この関数内で外側にあるdequeへのpush (append) をやっていてちょっと見通しが悪い。

もとの二分木に含まれるインスタンスを使い回すと結構シンプルに書ける（子ノードも引き連れた状態になっているので）。

#### https://github.com/naoto-iwase/leetcode/pull/22

dequeを使った実装 (step3). root1にマージすることで破壊的にやっているが、

>非破壊でやるならroot1 = copy.deepcopy(root1)を追加すればいいだろう。

とのこと。冒頭でdeepcopyすれば非破壊になる。なるほどー。

ところでdeepcopyすると、子ノードもコピーされるんだろうか。リファレンスを見てみる。  
https://docs.python.org/3.13/library/copy.html

>A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

なるほどー。いちおうコードも書いて確認した。

>考え方の一つとして、キューに入れるオブジェクトにNoneが入る可能性を排除する（型安全性）が良い方法に繋がった気がする。

こちらもなるほど。

#### https://github.com/nanae772/leetcode-arai60/pull/23

スタックを使った実装 (step3). スタックには `(node1, node2, マージ先の親, 左or右)` をpushする。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.cxy3cik6kyqx

破壊or非破壊の議論。ちゃんと気にできていた。

https://discord.com/channels/1084280443945353267/1295357747545505833/1329746604114055191

stackに `(マージ先, マージ元のlist)` を持っておく形。これはスッキリしてて良いかも。

https://github.com/tarinaihitori/leetcode/pull/23#discussion_r1919824481

>Python は、メンバ変数へのポインターが持てないので、どうしても繰り返し感がでますね。

>C++ だとどこに書き込むかをスタックに積むことができるので、少し簡単になるのです。

なるほど。Pythonだとsetattr, getattr, attrgetterあたりを使うことで近いことはできる。

## step 3

自分には、本問では再帰のほうがしっくりきた。

