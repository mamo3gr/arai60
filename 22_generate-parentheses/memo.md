## step 1

カッコのペア数 `n` が与えられたとき、すべてのwell-formedなカッコの組み合わせを列挙する。
制約として `n` の値域は `[1, 8]` である。

まずはスタックを使って状態を引き継いでいくのが素直そうに感じる。
作成途中のカッコ `parenthesis` と、カッコを開いた数 `num_opens`, 閉じた数 `num_closes` のタプルを引き継ぐ。2つの数は `parenthesis` をスキャンすれば分かるが、popのたびにやるのは手間だろう。
状態を引き継いだら（popしたら）、それぞれ可能であれば、カッコをひとつ開いた状態と、カッコを閉じた状態に分岐して、それぞれをスタックに積めばよい。

これまた計算量の見積もりが難しそう。コードを書いた後でGeminiに手伝ってもらう。
出力の数を書き出してみると、`n = 1, 2, 3, ...` で1通り、2通り、5通り、…とカタラン数になっているらしい。
カタラン数の一般項は 2nCn / (n+1). これには 4^n / {n^(3/2) x sqrt(pi)} という近似式があるらしい。
`n = 8`, Pythonの処理能力を10^7 steps/sec とすると、
4^8 / {8^(3/2) * sqrt(pi)} / 10^7 = 513マイクロ秒くらいのオーダー。
メモリ使用量については、スタックには最大 `n` の、作成途中のカッコを含む状態が積まれる。
積まれる状態は、長さ平均 `n`（完成で `2n` だから）のstr、あとはint 2つ。
つまり、8 * (8 * 4 bytes/str + 2 * 24 bytes/int) = 640 bytesくらいのオーダーを予想する。

## step 2

スタックを使わずに「push, 再帰、pop」の形式に書き直す。

### 他の人のコード

#### https://github.com/h1rosaka/arai60/pull/54

現在のカッコの組み合わせ `parentheses` と、開き-閉じの数 `left_surplus` をスタック経由で引き継ぐ (step1).
最初は必ず開きカッコから始まるので、はじめに `"("` と `1` を積める。
popしたら、開きカッコが続く場合・閉じカッコが続く場合とを、カッコの対応は気にせずにスタックに積んでしまう。
対応が正しいかはpop時にチェックする。`left_surplus` が負なら不正なので、それ以上は進めない。

終了条件について、自分は `num_opens == num_closes == n` としていたが、
`len(parentheses) == 2 * n` も成り立つ。なるほど。

#### https://github.com/Satorien/LeetCode/pull/52

`n-1`での結果に対して1ペアカッコを付ければ`n`での結果になる (step1).

>前のやつの全体を囲うか()を前後につけるか

https://github.com/olsen-blue/Arai60/pull/54#discussion_r2027288220

>はじめの括弧とそれに対応する括弧に注目して「(A)B」と分けるのも分類

この形を決めて、あとは`A = func(i)`, `B = func(j)`, where `i + j = n - 1` となる組み合わせ
すべてでやってみればよい。

面白いので自分でも書いてみる。3重forで書くより、AとBは `itertools.product` の方が意図が伝わるかと思う。

作成途中のカッコ `paren`, 開いた数 `opened`, 閉じた数 `closed` をスタックで引き継ぐ形 (step3).

1. `opened == n` なら残りは全部閉じる、
2. `opened` をインクリメントした形をスタックに積む、
3. （可能なら）`closed` をインクリメントした形をスタックに積む。

1. の閉じは、3. でもできるはずなので、ここでは最終結果にappendできるかどうかだけを判定するのが
見通しが良いように感じる。

#### https://github.com/naoto-iwase/leetcode/pull/54

枝刈り付きのBFS（実装1）.
`combination: list[int]`, `diff: int = num_open - num_close` からなる状態を
`frontiers: list[tuple[list, int]]` で複数持っておく。
できるカッコは必ず長さ `2n` になるので、2n回のループを回して、それぞれの状態を更新していく。
更新では、足せるなら `(` と `)` をそれぞれ足す。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.lqk42foli42r

https://github.com/fhiyo/leetcode/pull/53#discussion_r1714137722

Pythonはネイティブコードなら速い（C相当）。

https://github.com/frinfo702/leetcode-arai60/pull/10#discussion_r1881386807

>計算量はあくまでも極限での振る舞いなので、計算量を使って計算時間を見積もるのが大事です。
>
>また、速度が速いかどうかは、普通コーディングにおいてそれほどプライオリティーが高くないです。

>code complexity, memory, speed あたりのバランスで選ばれることが多いです。基準としては、将来、問題を起こさない可能性が高いと思われるものが選ばれます。エンジニアリングをするということですね。

https://github.com/olsen-blue/Arai60/pull/54#discussion_r2020125121

>これは解の空間をどう分けるか、分類するかの考え方で網羅的に分類できていればなんでもいいのです。

仕事の単位と引き継ぎ。

https://discord.com/channels/1084280443945353267/1339428945845555252/1381993770840756226

文字列のコピーを避けるために高階関数を使う例。

https://github.com/skypenguins/coding-practice/pull/27#discussion_r2533462366

* strはimmutableなのでカッコを足す都度再構築される。list + listも同様。
* この問題では再構築のコストはそれほど目立たない。
* 文字列のコピーは速い。
  * 100倍くらいらしい。つまりここだけC相当。

