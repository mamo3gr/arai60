## step 1

整数の配列 `candidates` が与えられたとき、和が `target` になる組み合わせをすべて列挙する。ただし、`candidates` の要素は何回使ってもOK. 制約は次の通り。

* 1 <= `candidates.length` <= 30
* 2 <= `candidates[i]` <= 40
* 1 <= `target` <= 40

`candidates = [2,3,5]`, `target = 8` の例を考えてみる。
`candidates[0] = 2` を `target` を超えるまで組み合わせ `combination: list[int]` に足していって、`candidates[1] = 3` を超えるまで足していって…、をやれば良さそう。
ここまでのバックトラッキング問題で覚えた、ホワイトボードとして `combination` と `total` とを共有しつつ再帰するパターンで書く。

処理時間とメモリ使用量の見積もりが単純ではない。
問題の制約から外れてしまうが、`candidates = [2] * 30` と `target = 40` のときを考えて、上限を求めてみる。
処理時間は、`candidates[i]` を 40 以上になるまで足す（20回）、を `i = 0, 1, ..., 29` （30種類）の組み合わせでやるので、30^20 になる？上限にしてもちょっと時間がかかりすぎる。
現実的には、`candidates` の要素の値域は `[2, 40]` なので、中間の20くらいを使うのが良さそう。
そうすると 30^2 くらいか。Pythonの処理能力を 10^7 steps/sec とすると、
30^2 / 10^7 = 90マイクロ秒くらいのオーダーを予想する。

次にメモリ使用量を考える。再帰の深さは、`len(candidates)` と等しい。つまり最大30である。
スタックフレームあたり150 bytesとすると、最大 30 * 150 = 4.5KB くらいのオーダー。
途中の組み合わせ `combination` は、平均で40/20 = 2要素くらい、最大で20要素が入る。
20 * 28 bytes/int = 560 bytes くらいのオーダー。

## step 2

GeminiとChatGPTにレビューしてもらいつつ整理・改善する。

* `candidates` をソートしておくと、`total` が `target` を超えた時点で探索を打ち切れる
  * それ以降の `candidates` を足しても `total` に等しくなることがないので
* `total` を nonlocal で共有するのでなく、関数の引数として `remining` を渡すとよい
* 再帰一度につきappendする数字はひとつのほうが可読性が高い

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/52

次に使用を検討する `candidates` のインデックス `start`, ここまで作った途中の `combination: list[int]` を引き継いでのバックトラッキング (step1).
和は都度 sum で計算している。この和も引き回したほうが良さそう。可読性も損なわない。

https://github.com/garunitule/coding_practice/pull/52/changes#r2791623772

>返り値の型ヒント -> None をつけた方が、何も返らないはずである（ということは副作用がある？）ことが明確になって読みやすいかもしれません。

これはそうだなあ。読み手として安心する。

`combination, total, start` のタプルをスタックに積む、という変形もできる (step2).
あるいは、`combination` は参照をコピーするか、スタックの外で管理する、というパターンもありそう。
メンタルモデル的にはコピーしたものをスタックに積みたい。前述のタプルがステート（スナップショット）で、
それは他のステートと共有されていてほしくない（動作的には問題ないが）。

#### https://github.com/h1rosaka/arai60/pull/53

`combinations`, `start` を引き回すバックトラッキング。スタックを使っている (step1).
n分木、2分木として捉えているのが面白い (step2).

#### https://github.com/huyfififi/coding-challenges/pull/43

`combinations_found: set[tuple[int, ...]]` で重複排除を意図している (step1) が、
バックトラッキングの順序を整理すれば重複は起こらなさそう。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.vo5b5dbpqng

https://github.com/fhiyo/leetcode/pull/52#discussion_r1690161771

>この問題ですが、基本的にはバックトラックをするわけですが、
>分類してみると、いくつかあるように思います。
> 
>[A, A] まで使うことが確定していて B 以降しか使ってはいけないという状況下で、
> 
>    1. Bを一つ使うか、C 以降しか使ってはいけないか、に分岐する。
>    2. Bの使う数を列挙して分岐し、C 以降しか使ってはいけないに遷移する。
>    3. 次の1個が、B, C, D, E, F... である場合に分岐する。
> 
>あたりのように思っています。
>とにかく、抜け漏れなく分類ができれば、いいということでしょうか。

なるほどなー。選択肢の幅。
step1は2. だな。step2では3. にしている。
1. はBを2つ以上使い場合が漏れちゃいそうだけど大丈夫なんだろうか。

https://github.com/Mike0121/LeetCode/pull/1#discussion_r1578212926

>答えの数ですが、candidates = [1..target] の場合、これは分割数というものですね。

分割数という概念は知らなかった。

https://discord.com/channels/1084280443945353267/1233295449985650688/1242118169968115845

計算量のざっくりとした見積もり。
