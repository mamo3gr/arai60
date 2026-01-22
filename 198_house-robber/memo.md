## step 1

数列 `nums` が与えられて、いずれも隣接しない要素からなるsubarrayを考えたとき、最大の和を求める問題。  
`max(奇数インデックスの和, 偶数インデックスの和)` で解けるのかと思いきや、もうひとつ飛ばしの方が和が大きくなるケースがあった。

短い `nums` から考えてみる。  
長さ1のときは自明で `nums[0]`.  
長さ2のとき、`nums[0]` か、`nums[1]` のmaxになる。`f(i)` を `nums[:i+1]` での最大和とすると、`f(0)` と `nums[1]` のmaxを取る、と書ける。  
長さ3のとき、`nums[2] + f(0)` か `f(1)` のmaxを取れば良い。  
つまり一般化すると、`f(i)` は `nums[i] + f(i-2)` と `f(i-1)` のうち大きい方である。

再帰で書くのがシンプルに見える。Tabulation（テーブルを使ったボトムアップ）でも書けそうで、これはstep2でやる。

処理時間を見積もる。  
`f(i)` あたり `f(i-1)` と `f(i-2)` の2つがコールされる。呼び出しごとに `i` がデクリメントされているので、`i=0` にたどり着くには `N` 回の再帰が必要（数列の長さを `N` とする）。つまり `O(2^N)` で、`N` の最大は制約から400なので、2^400 / 10^7 というとんでもない時間がかかる（Pythonの処理能力を10^7 steps/secとする）。  
メモ化すると、`f(i)` がそれぞれキャッシュされるので、`i = 0, 1, ..., N` をそれぞれ計算するだけになり、`O(N)` と見れる。400 / 10^7 = 40マイクロ秒くらいのオーダーを予想する（簡単のためステップ数=1としている）。  
また、メモ化により、空間計算量も `O(N)` 必要になる。key=引数, value=結果のdictを想像し、どちらもintとすると、28 bytes/int * 2 * 400 = 22.4 KB くらいのオーダーを予想する。

## step 2

テーブルを用いたボトムアップのパターンも書いてみた。  
番兵を置くとメインのループがシンプルになるが、一方で `f(i)` のテーブルと `nums` とでインデックスがずれるのが悩ましい。

### 他の人のコード

#### https://github.com/naoto-iwase/leetcode/pull/40

`f(i)` を算出するときには、直前の `f(i - 1)` と `f(i - 2)` しか要らないので、これ以前の結果は記憶しない。メモリ使用量は抑えられる一方で、`with_last`, `without_last` とそれぞれの `next_` が出てきてお手玉感があり、読むのはわずかに負荷がある。

#### https://github.com/nanae772/leetcode-arai60/pull/34

直前の2つだけを記憶する場合の、命名の検討。

* `with_last`, `without_last` (naoto-iwase)
* `max_robbed_previous`, `max_skipped_previous` (nanae772)
* `max_one_step_ago`, `max_two_step_ago` (garunitule)

#### https://github.com/garunitule/coding_practice/pull/35

`if not nums` で0を返す。raiseするのとどっちがいいかなあ。  
個人的には、空はユーザーの想定外（ミス）のような気がするので、raiseするほうが事故が起こらないと思う（空ならそもそもユーザーはこの関数を呼ばないし）。

### コメント集

#### https://github.com/Mike0121/LeetCode/pull/47#discussion_r1799964450

>functools.lru_cacheを確認しておいて欲しいのと、inner function は定義するたびにオブジェクトとして作り直されていることを確認して欲しいです。
>
>このコードはスレッドセーフティーという意味でどうなっているでしょうか。

スレッドセーフだと書いてある。  
https://docs.python.org/3.13/library/functools.html#functools.lru_cache

>The cache is threadsafe so that the wrapped function can be used in multiple threads. This means that the underlying data structure will remain coherent during concurrent updates.

inner functionは `rob` メソッドが呼ばれるたびに生成され、キャッシュはこれ（のみ）に紐づくので、メソッド外からは読み出しも書き込みもされないと思う。

>あ、私がいいたかったのは、rob が同時に別のスレッドに2回呼ばれたとしても、中の memo, find_max_value は rob のローカル変数なので異なるものであり、問題なく動くということです。

そうだよね。意外なことがなくてよかった。

#### https://github.com/hroc135/leetcode/pull/33#discussion_r1899009212

>フィボナッチになりそうですね。黄金比の n 乗なので 1.6^n くらいです。

メモが無いときの時間計算量。  
`f(i)` の算出のとき、`f(i-1)` と `f(i-2)` が必要になる。それぞれの計算量を `g` で書くと `g(i) = g(i-1) + g(i-2) + C` で、このフィボナッチ的な関係式を解くと黄金比が出てくるらしい。

## step 3

直前の2つだけを記憶するバージョンに挑戦。  
`robbed_last`, `skipped_last` がしっくりきた。  
`skipped_last` は `max(robbed_last, skipped_last)` で更新するのがハマりポイント。
