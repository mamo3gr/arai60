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

使うメモリは、visitedを管理するのにint2つを最大 `M * N`. 28 [bytes/int] * 2 * 300 * 300 = 5 MBくらい。  
島ごとの探索中も同じくらいなので、10 MB程度を想定。

途中、ループカウンタを上書きしてしまうバグを踏んだりしたが、何とか答えを見ずにテストケースを通せた。
