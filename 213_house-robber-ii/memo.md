## step 1

[198. House Robber](https://leetcode.com/problems/house-robber/) のアレンジ版。  
数列 `nums` が与えられて、隣同士隣接しない要素からなるsubarrayを考えたとき、最大の和を求める。
ただし、数列の最初と最後は隣接している（これが前問と異なる点）。

前問と同様に、`nums` を `i` 番目までに区切って考えてみる。`nums[:i+1]` が入力のときの最大和を `f(i)` と書く。テストケースは `[1, 2, 3, 1]`.  
`i=0` のとき、`f(0) = nums[0] = 1`.  
`i=1` のとき、`nums[0]` か `nums[1]` のどちらか。`f(1) = max(nums[0], nums[1])`  
`i=2` のとき、`nums[0]` か `nums[1]` か `nums[2]` のいずれか。前問では `nums[0] + nums[2]` を取れた。  
`f(1)`, `nums[2]` って書けるか。  
`i=3` のとき、`nums[0] + nums[2]`, `nums[1] + nums[3]` のいずれか。  
つまり、`f(i-3) + nums[i-1]`, `f(i-2) + nums[i]` って書ける？  
いやいや、`f(1) = f(0) = nums[0]` だったとき、先頭と終端を取っているので制約を破っている。

詰まってしまったので、LeetCodeのヒントを読む。

>Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money.

ほぼ答えじゃん…。

tabulationのパターンは後で書くとして、まずは再帰＋メモ化で書いてみる。  
`self.rob()` の中で `self.rob(nums[:-1])` と `self.rob(nums[1:])` を呼ぶと、
スライスがコピーされる（無駄）。
また、inner functionをメモ化すると、それぞれのサブ問題を解くときのキャッシュが衝突する。  
したがって、`self.rob_sub()` のような別メソッドを生やせば、後者は回避できる。
前者（冗長なメモリコピー）は、`len(nums)` が高々100であることから、可読性の方を優先する。

計算時間を見積もる。  
`N = len(nums)` とすると、メモ化しているので `O(N)` と見れる。
`nums[:-1]` と `nums[1:]` とで2回計算しているが、これは定数倍になるのでオーダーには効かない。  
100 * 2 / 10^7 steps/sec = 20マイクロ秒くらいのオーダーを予想する。
必要なメモリは、スライス `nums[:-1]` と `nums[1:]` をコピーするための `N-1` 個のintで、28 bytes/int * (100-1) = 2.8 KB.
メモ化は辞書で管理される認識で、key=インデックス、value=結果とすると、2 * 28 bytes/int * 100 = 5.6KB.

## step 2

Geminiと解法についてディスカッションしてみた。
one-passのDPで解けないのは「`nums[0]` を取ったかどうか」を覚えておけないから。
円環問題を解くときには、直線2つに分けて考えるのが定石らしい。実際の面接で、小さなヒントからここにたどり着けるかなあ。

tabulationのパターンも書いてみた。これなら範囲の始点と終点だけを引き回せばいいので、スライスのコピーが要らなくなる。

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/36

2変数だけを記憶するtabulation. 変数名は `max_{one,two}_step_ago`.  
メインに入る前の場合分けは、`not nums` と `len(nums)==1`. この2つのほうが分かりやすいかも。

#### https://github.com/naoto-iwase/leetcode/pull/41

2変数だけを記憶するtabulation. 変数名は `without_last`, `with_last`.  
変数の更新でmultiple assignment（多重代入、複数代入）を使っている。  
これなら `next_` のような一時変数が不要になる。

```python
        def rob_section(left, right):
            without_last = 0  # max total without robbing last house
            with_last = 0  # max total with robbing last house
            for i in range(left, right + 1):
                without_last, with_last = (
                    max(without_last, with_last),
                    without_last + nums[i]
                )
```

https://github.com/naoto-iwase/leetcode/pull/41/changes#r2478782275

>私はこの書き方あまり好きではないですが、まあ、しかし新しい変数作るよりは見やすいかもしれませんね。

意図不明の `next_` が出てくるよりは、依存関係がある2変数を更新したい、という意図が分かるので、多重代入の方がマシに思える。

#### https://github.com/Mike0121/LeetCode/pull/57

https://github.com/Mike0121/LeetCode/pull/57#discussion_r2425654031

>この場合、単に 引数の nums を円形制約なしで盗んでいるので、関数内関数でなく独立した rob_linearly のような関数とした方がわかりやすいと思いました。

`linearly` なるほど。

### コメント集

なし。
