## step 1

1=島、0=海の2Dグリッドが与えられたとき、島の数を数える。連結は上下左右。  
すべての島について、島ごとに番号を振っていけば良い。

右上から左下に向けて探索していけばいいのではないか？と思い以下の実装をしてみたが、「エ」の字のような枝分かれのケースに対応できなかった。

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                
                known_island = False
                if i - 1 >= 0 and int(grid[i - 1][j]) > 1:
                    grid[i][j] = grid[i - 1][j]
                    known_island = True
                
                if j - 1 >= 0 and int(grid[i][j - 1]) > 1:
                    grid[i][j] = grid[i][j - 1]
                    known_island = True

                if not known_island:
                    num_islands += 1
                    grid[i][j] = num_islands + 1

        return num_islands
```

いま（新しい島か）判定しようとしている島から、上下左右の島をキューに入れていき、順にvisitedか調べる。
キューが尽きてもvisitedの島に到達できないなら、新しい島である。このとき、キューに入れたかどうかをsetで管理する（そうしないとキューにループして島が入る場合がある）。スタートした島をvisitedにする。

時間を見積もる。グリッドが `M x N` なので、外側のループで `O(M * N)`, 島ごとの判定も `O(M * N)`.  
つまり `O(M^2 * N^2)`. `M` も `N` も最大300なので、最大のケースで 300^2 * 300^2 / 10*6 [step/sec] = 8,100 秒。島ごとの判定について上振れすぎている気もする。

使うメモリは、visitedを管理するのにint2つを最大 `M * N`. 28 [bytes/int] x 2 x 300 x 300 = 5 MBくらい。  
島ごとの探索中も同じくらいなので、10 MB程度を想定。

途中、ループカウンタを上書きしてしまうバグを踏んだりしたが、何とか答えを見ずにテストケースを通せた。

## step 2

探索するついでに島をvisitedに入れちゃえば良さそう。

### 他の人のコード

https://github.com/docto-rin/leetcode/pull/17

- `queue` に何を入れているのか、名前に入れる。
- `grid` を破壊しない、はできていたが、setを使う vs. `grid` のコピーを作ってそれを使う、の検討はできていなかった。島が疎な場合はsetの方が省スペースだが、ハッシュ計算のオーバーヘッドがある。実務なら与えられるデータ（グリッド）の傾向から判断かな。
- 範囲外か、島かの判定を関数に括りだすのはいいな。
- 増分を `[1, 0], [-1, 0], [0, 1], [0, -1]` とiterativeで書くのもよい。
- キュー (FIFO) なら BFS（Breadth-First Search, 幅優先探索）、スタック (LIFO) なら DFS（Depth-First Search, 深さ優先探索）になるらしい。前者はスタートから探索範囲を広げていくイメージ。後者は行ける先までとにかく行って戻って来るイメージ。
- 再帰でも書ける。がスタックオーバーフローしそうだしあんまりメリットが思いつかない。可読性は上がるか…？

https://github.com/Yuto729/LeetCode_arai60/pull/22

- `traverse` という語彙を自分の辞書に追加。
- `WATER` とか `LAND` とかを定数にするの良いね。
- Union-Findという解法も。はじめにすべての島が独立な状態だと考えて、隣接する島同士をグルーピングする。その際に `num_islands` をデクリメントする。

https://github.com/Kaichi-Irie/leetcode-python/pull/28

- 『境界チェックは 「数直線に沿った」条件式が望ましい』たしかに。
- 『もしこのグリッドが非常に巨大で、例えば数テラバイトあり、メモリに一度に収まらない場合はどうしますか？』→このケースでUnion-Find (Disjoint Set Union: DSU) が役に立つらしい。グリッドをメモリに乗る範囲で一部ずつ処理できる。

https://github.com/Shoichifunyu/shofun/pull/12

- 『繰り返すところで、違和感と向き合う』

https://github.com/yas-2023/leetcode_arai60/pull/17

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.6z8kd1z4d8gp

https://github.com/sakupan102/arai60-practice/pull/18#discussion_r1582241335

>将来、これをデバッグするのは自分ではない誰かと思われるので、これを条件に当てはまらないときに呼ぶと例外が投げられる、呼んだやつが悪い、というのはあまり好ましい態度ではないと思うわけです。

この「引き継ぎ」の態度、大事にしていこう。

## step 3

- 島がまあまあ密であることを想定して、訪問済みの島はboolの2次元配列で管理することにする。
- 読みづらい処理はクラスのメソッドに切り出す。メソッド内に関数を定義することも考えたが、インデントがもう位置上がるのが嫌。一方でメソッド呼び出しのオーバーヘッドはかかる。

## TODO

- [ ] DSU (Union-Find) でも解いてみる
