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
