## step 1

整数の配列 `nums` が与えられたとき、すべての `0` を配列の後ろに移動させる。
非ゼロの要素は、それらの順序を維持する。また、この操作はin-placeでやれ、とのこと。
`N = nums.length` は最大 10^4.

例の `[0,1,0,3,12]` を使って、手作業でやってみる。
左から舐めていって、ゼロを見つけたら、最左端の非ゼロ要素と入れ替えていく、のかな。
このようなブルートフォースでやると、`O(N^2)` かかる。
`for i in range(len(nums))` に対して `for j in range(i, len(nums))` を舐めるので、
N + (N - 1) + ... + 1 = N(N+1)/2 回の走査になる。
`N` の最大数を代入し、Pythonの処理能力を10^7 step/secとすると
10^4 * (10^4 + 1) / 2 / 10^7 = 5秒のオーダー。終わるかどうか微妙なところ。

処理時間を短縮するため、一度だけ舐めることを考える。
ゼロが見つかるたび、インデックスをキューに入れる。
非ゼロが見つかったら、キューの先頭のインデックスを取り出してswap.
swap後のインデックスをキューに入れる。
これで時間計算量は `O(N)` になりそう。空間計算量も `O(N)`.
処理時間は10^4 / 10^7 = 1ミリ秒オーダーになりそう。
キューには最大 `N` のインデックスが入る。10^4 * 28 bytes/int = 280 KBくらいのオーダーを予想する。

これはin-placeと言っていいんだろうか…？
空間計算量が `O(N)` で、これは `nums` の（部分的な）コピーを取った場合と変わらない。
そこで、ダブルポインタを使った解法も書くことにする。
ゼロが非ゼロの左側にあるときだけswapすべきだし、そうでないならゼロの右側に対して更に非ゼロ要素を
探しに行く必要があることがハマりポイントだった。

## step 2

片方を for で強制的に回すのが分かり良いような気がしてきた。ので書き直してみる (step2-1.py).
さらにGeminiにレビューしてもらう。「次に非ゼロ要素を配置すべきインデックス」を覚えておくのが
スマートらしい。随分シンプルになった (step2-2.py).

### 他の人のコード

#### https://github.com/h1rosaka/arai60/pull/55

最後に非ゼロを置いたインデックス `max_non_zero_index = -1` を覚えて更新するパターン (step1).
自分の解法でいう step2-2 と一緒だが、`nums[max_non_zero_index + 1]` をswapしにいく必要がある。
「次に」更新するインデックスのほうが自然に感じる。

問題の名前が "Move Zeroes" だったので「ゼロを動かす」のだと引っ張られたが、
「（非ゼロを動かして）ゼロを埋める」方が実装としては素直なんだな。
手作業ではできたが、問題のリフレームの幅が狭かった。

#### https://github.com/Satorien/LeetCode/pull/53

先頭から舐めて、ゼロを見つけたらpopしてappendする、つまりお尻に持っていく (step1).
自分では思いつかなかったシンプルな実装。ただし時間計算量は `O(N^2)`.
後ろがゼロだけになった場合、無限にpop & appendしてしまうので、
全体で見つけたゼロの個数 `zero_count` を覚えておいてpop & appendの回数制限に使う。

https://github.com/Satorien/LeetCode/pull/53/changes#r2659028220

erase remove idiom というのがあるらしい。

https://en.wikipedia.org/wiki/Erase-remove_idiom

>The erase–remove idiom is a common C++ technique to eliminate elements that fulfill a certain criterion from a C++ Standard Library container.

`vector` などのコンテナの要素を `erase` すると、後ろの要素を詰めるオーバーヘッドが生じる（Pythonの`list.pop()` のようだ）。
そこで `remove` と組み合わせる。`remove` は与えた条件を満たす要素を取り除き、有効な（条件を満たさない）要素を前に寄せる。戻り値として有効な要素の次を指すイテレータを返す。
`remove` で取り除きたい要素（本問でいうゼロ）を後ろに寄せた後、戻り値のイテレータから末尾までを `erase` することで、コンテナから望む要素をまとめて消せる。

#### https://github.com/docto-rin/leetcode/pull/55

先頭から舐めて、ゼロを見つけたらpop (remove). popした回数を覚えておいて、
最後に元の長さになるように末尾にゼロを足す（実装1）。
`nums` を舐めるので `O(N)`, 任意の位置での `list.pop()` が `O(N)` かかるので全体の時間計算量は `O(N^2)`. ただし補助空間は `O(1)` で済む。

自分の step2-2.py ではスワップしていたのに対し、スワップではなく非ゼロ要素を書き込み、
最後に末尾までゼロをfillするというパターンもある（実装3）。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.v62rdhwkdymb

https://github.com/fhiyo/leetcode/pull/54#discussion_r1720791348

>もし時間にめちゃくちゃシビアな場合は、Step2の①の別解のスワップしない実装の方が速そうですね。（そんなシビアな事をpythonでするなという感じもありますが）
>ただ、この方法の方が意味がわかりやすいのと、仮に仕様変更で0ではなくて0以下を端に寄せたいとなった場合にもcontinueする条件をnums[i] <= 0とするだけでワークするので、良いと思います。
>
>この辺、3rdで最終的にこの方法を選んだ理由や考えが明示されていると良いかもしれないですね。

良し悪しの洗い出しと判断。

https://github.com/fhiyo/leetcode/pull/54#discussion_r1729801172

Generatorを使ったパターン。
ゼロ要素のインデックスだけを返すGenerator `eq0` と、
非ゼロ要素のインデックスだけを返すGenerator `neq0` を用意する。
`next(eq0)` でゼロ要素のインデックスを取り出した後、
それよりも右のインデックスを（あれば）`neq0` から取り出して、要素をswapする。
Generatorがもう値を出力できなくなると `StopIteration` が早出されるので、
まるっと `try-except` して脱出する。

自分のstep1.pyと同値の実装。whileでポインタを進めるにしろ、Generatorでインデックスを取り出すにしろ、
終端まで行ったときの処理が面倒だし読みづらい。

https://github.com/olsen-blue/Arai60/pull/55#discussion_r2024137192

`next` の第2引数 default を使うと `try-except` は不要になる。
にしてもwhileを抜けるパターンがちょっとパズルっぽい。

https://github.com/rihib/leetcode/pull/50#discussion_r1888189547

>これ C++ だと zeroIndex == i の場合は未定義動作にあたるかと思いますが、Go では大丈夫でしょうか。
>
>この質問は、本当に不安に思っているというよりは、言語仕様を調べたことがありますか、それとも漫然と経験上書いていますか、という質問です。

当然問題ないと思っていたけど調べてなかった。

https://docs.python.org/3/reference/simple_stmts.html#assignment-statements

>An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

>Else: The object must be an iterable with the same number of items as there are targets in the target list, and the items are assigned, from left to right, to the corresponding targets.

https://github.com/hroc135/leetcode/pull/51#discussion_r2052911267

Linked Listなら、頭から舐めてゼロならお尻に移す、が `O(1)` でできる。
自分でも書いてみよう (`step2_linked_list.py`)
