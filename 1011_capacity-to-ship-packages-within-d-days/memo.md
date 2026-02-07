## step 1

荷物の順番と重さ `weights: list[int]` と、日数 `days: int` が与えられたとき、
`days` 以内で荷物を運ぶための船の最小の積載量 `capacity: int` を求める。
制約は、`days` と `len(weights)` の最大が 5 x 10^4 で最小が 1, `weights[i]` は最大500.

テストケースを見ながら手作業でどうやるか考えてみる。
例えば、`weights = [1,2,3,4,5,6,7,8,9,10]`, `days = 5` だと、求める解は 15 になる。
`[1,2,3,4,5]`, `[6,7]`, `[8]`, `[9]`, `[10]` の5日で運べば良い。
これよりも小さい14だと、`[1,2,3,4]`, `[5,6]`, `[7]`, `[8]`, `[9]`, `[10]` となり6日かかってしまう。

ここで気がついたのは、`capacity` が与えられれば、`weights` を `days` 以内で出荷できるかを
`O(N)` で判定できる。ただし、`N = len(weights)` である。使うか分からないが…。

適当に下限と上限を決めて、`capacity` を二分探索する、とかかな
（問題のカテゴリが二分探索だから、というズル）。
`weights` の隣接する要素同士をグルーピングして、グループ数が `days` になったら sum の max を取る、
みたいなやり方もありそう。ただ、どの要素を、左右どちらの要素と吸収合併させるかを選ぶのは難しそう。
その時点での最小を取ってきて、左右の小さい方と…、みたいにやるんだろうけど、
合併するたびに `weights` を更新したり、その中の min を探す、というのは面倒。

考えすぎている気もするので、最初の方法で手を動かしてみる。
`capacity` の下限は1だろう（それよりも小さい0だと運べない）。
上限は、`weights[i]` が最大500, `len(weights) = 5 * 10^4`, `days = 1` のときで
500 x 5 x 10^4 とすれば良い。

処理時間とメモリ使用量を見積もる。
時間計算量は `O(N x logN)`. `N` の上限が 5 x 10^4で、Pythonの処理能力を 10^7 steps/sec とすると、
5 x 10^4 x log(5 x 10^4) / 10^7 = 78ミリ秒くらいのオーダーを予想する。
空間計算量は `O(1)`. 具体的には、二分探索する上限と下限。サブルーチンでは経過日数と現在の積載量。

何とかテストをパスした。引っかかったのは

* 二分探索での上限・下限の更新。無限ループしてしまっていた
* サブルーチン（`capacity`, `weights`, `days` が与えられたとき、出荷が間に合うかの判定）にて、
  日数の初期化ミス
* 上限の初期化ミス。500 x 5 x 10^4 は大きすぎじゃ？と思って `ceil(500 * N / days)` にしていたのだが、
  正しくは `500 * ceil(N / days)`.

このメモを書くのも含め1時間かかってしまったが、解答を見ずにパスしたのは久しぶり。

## step 2

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/44

方針は一緒。
サブルーチンに切り出すのも一緒だが、`bool` ではなく所要日数を返して、
メインルーチンでdays以内か判定している。
好みの範囲だろうが、daysを計算する方が、メインルーチンでの二分探索の更新がバグりにくそうだし、
汎用的に使いまわせそう。

>"""
>不変条件
>- capacity < left_capacityの場合、daysより大きい
>- right < capacityの場合、days以下
>"""

こういうのちゃんと書くべきだった。反省。

初期値の決め方。

```python
        # len(weights)分だけ日数がかかる
        left_capacity = max(weights)
        # 1日で運べる
        right_capacity = sum(weights)
```

自分は複雑に考えてたけど、これはシンプルだ。
将来的に制約（例えば荷物あたり500とか）が変わっても対応できる。
あと自分の場合は、下限を低く取りすぎて `weight <= capacity` のチェックをする羽目になっていた。

#### https://github.com/h1rosaka/arai60/pull/46

daysを二分探索する方針は一緒。サブルーチンが面白い。

```python
def can_ship_within_the_period(capacity) -> bool:
     i = 0
     for _ in range(days):
         total_weight = 0
         while total_weight + weights[i] <= capacity:
             total_weight = total_weight + weights[i]
             i += 1
             if i == len(weights): # 載せきった。
                 return True
     return False
```

for each daysで回して、その中で積めるまで積む、というロジック。
こっちのほうが手作業に近い。
一方でコードとしてはちょっとぎこちない感じに見える。

#### https://github.com/naoto-iwase/leetcode/pull/27

`bisect_left` を使った実装。`range(capacity_high)` を渡すと、
ありえる値の範囲をリストとして実体化しなくてもいい。
`key` に `days` 以内に出荷できるか判定する関数を渡す。

自分でも書いてみよう。
`bisect_left` がインデックスを返すところだけ注意。
第一引数に `(min, max+1)` を渡して後で min で下駄を履かせるか、
引数 `lo` に min を渡すかする。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0 を `capacity`, `ship` や `1011` で検索してみたが見つからず。

## step 3

練習も兼ねて、二分探索を自分でやる方を書き直す。
個人的にはinner functionよりもstaticmethodで出すほうが好み。
この量ならギリギリinner functionにしてもいい。

lower,upperは求める値を含むのかどうか分かりにくいので、素直にmin, maxにした。

