## step 1

文字列 `s` と `t` が与えられたとき、`s` が `t` のsubsequenceであるかを返す。
それぞれ英語の小文字のみを含み、最長は `s` で100, `t` で10^4である。

`for c in s` に対して、`t` の先頭から同じ文字を探していく、でできそう。
探すには、

* いま `i` 文字目である、というポインタを動かしていく
* `str.find()` を使う
* Generatorを使って1文字づつ出力する

が思いつくが、だいたいこの順で複雑さが無さそう。まずは1番目の方針でいく。

時間計算量は `O(N)`.
Pythonの処理時間を10^7 steps/sec とすると、10^4 / 10^7 = 1ミリ秒くらいのオーダーを予想する。
空間計算量は `O(1)`.

`s` の文字列 `c` とマッチしたときに `t` のポインタも進める必要がある、
というところで一度引っかかってしまった。

## step 2

step 1で思いついた他の書き方もやってみた。
加えて、Geminiによるコードレビューも反映した。

### フォローアップ問題

フォローアップ問題も考えてみる。

>Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

複数の（かつ大量の） `s` が来るのを捌く。
Geminiによると「各文字が `t` のどこに出現するかをあらかじめ記録しておく」らしい。
これは `char_to_indices: dict[str, list[int]` でできる。
で、`for c in s` に対して、`char_to_indices[c]` を引くと、
`c` が `t` に出現するインデックス（昇順）が取れる。
「いま `t` の何文字目まで進んだか」を `t_i: int` で覚えておいて、
`t_i + 1` が `indices` のどこにinsertできるか？を `bisect.bisect_left` で探せばいい。
これが右端になるようなら、もう `t` には出現しないので False を返す。

これで時間計算量が `O(logN)` になった。
ただし空間計算量が `O(N)` 必要。

### 他の人のコード

#### https://github.com/h1rosaka/arai60/pull/56

step3のコードが分かりやすい。

>t,s両方先頭から見て、両者が同じなら両ポインタを進める。違う場合は、t(削る方)だけ進める。
>sかtのポインタが範囲外になったら終了
>sのポインタが範囲外になってれば、sは全部見つかったということなので、True

#### https://github.com/Satorien/LeetCode/pull/56

index (i) と書くときは、`s` と `t` のどっちのインデックスなのか分かりやすいほうが見通しがいい。
どこまでか分からないがポインタを進めるならforよりwhileの方がしっくりくる。

#### https://github.com/naoto-iwase/leetcode/pull/58

ダブルポインタによる解法（実装1）。
`t_i` はどちらにしろ進めるから、`s[s_i] == t[t_i]` の条件分岐から出してもいい。
が、どちらにも書いたほうが自然言語での説明に近い気もする。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.ftci24or3a8g

https://discord.com/channels/1084280443945353267/1225849404037009609/1243290893671465080

ダブルポインタの変形パターン。
関数型っぽい見え方として、

* `s[0] == t[0]` なら `s[1:]` と `t[1:]` がどうか調べる
* そうでないなら `s` と `t[1:]` がどうか調べる

とも見える。
つまり再帰的にも書ける。
