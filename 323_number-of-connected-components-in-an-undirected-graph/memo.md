## step 1

`n` 個のノードからなる方向なしグラフが与えられたとき、"島"の数を数える。
エッジの情報は `[a_i, b_i]` のように与えられる。制約は次の通り。

* `1 <= n <= 2000`
* `1 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= a_i <= b_i < n`
* `a_i != b_i`
* There are no repeated edges.

いわゆる union-find で解けば良さそう。使うのはunionの方だけ。
はじめは各ノードが自身が親で、エッジで繋がることが分かれば親を統合する。
親は `parent: list[int]` で管理し、若い方を優先する。

親の伝搬を忘れて躓いてしまった。躓きそうなテストケースの想像が足りなかった。

処理時間とメモリ使用量を見積もる。
時間計算量は `O(n x e)`. ただし `e` はエッジ数。
for each edgeのループの中で、親の伝搬をするのに `n` 個のノードの親を舐める必要がある
（これは双方向に引けるようにしたら `O(1)` で済むのかも？ -> findするときに繋ぎ変えればよかった）。
Pythonの処理能力を 10^7 steps/sec とすると、
2000 * 5000 / 10^7 = 1秒のオーダー。なんとか終わるか。
空間計算量は `O(n)`. 各ノードの親を覚えておく必要がある。
28 bytes/int * 2000 = 56KB のオーダーを予想する。

## step 2

### 他の人のコード

#### https://github.com/Hiroto-Iizuka/coding_practice/pull/19

DFS. 隣接リスト `graph: dict[int, list[int]]` と、訪問済みノードを `visited: set` で覚える。

#### https://github.com/xbam326/leetcode/pull/21

DFSでは関数で再帰するほか、whileで書いちゃう幅もある (step3).

#### https://github.com/docto-rin/leetcode/pull/28

UnionFindで親を辿るための経路を効率化する方法があった記憶だが、ここに全部書いてあった。ありがたい。
findするときに、再帰的にfindして、rootにつなぎ替えてしまえばいい。
また、サイズが大きいgroupに小さいgroupをぶら下げたほうが、木の高さが抑制できるらしい。
これらを踏まえてもう一度書いてみる。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.aza5ygjw59gj

見出しだけあってリンクなし。

## step 3

DFS版は再帰するほどでもないので、スタックで書き直す。
ついでに開始ノードも合わせてvisitedにするように関数を変更する。

2ヶ月前に[Max Area of Islande](https://leetcode.com/problems/max-area-of-island/)を解いていた当時は
UnionFindをスクラッチで書ける気がしていなかったが、苦も無く書けるようになっていた。
