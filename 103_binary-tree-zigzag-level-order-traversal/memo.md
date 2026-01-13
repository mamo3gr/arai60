## step 1

与えられた二分木に対し、zig-zag order - つまり左→右、右→左、… の順でトラバースした結果（値）を返す。  
これ実務上はどんな応用があるのかな。→Geminiに聞いてみたが納得できる答えは得られなかった。

「いまどっち向きか？」を記憶しながら、上（根）からiterativeにキューに詰めていけば良い。積むときは末尾にappendして、popを先頭から・末尾からやる。dequeが良さそう。反対に、詰める時点で先頭・末尾に振り分けることもできそうだけど自分には不自然に思える。

時間計算量・空間計算量の議論は[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)と同様。同問を解いた https://github.com/mamo3gr/arai60/pull/25 を参照のこと。

前問のように、for each nodeで `val` の取得と子ノードのappendをやると、順番がこんがらがる。  
値は逆順でリストアップしたいが、子ノードは正順でappendしたい。どちらかだけを後でreverseするか、2回に分けてやるか。2重に走査するオーバーヘッドがあるが、後者のほうが分かりやすそう。

