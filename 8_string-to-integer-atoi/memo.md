## step 1

文字列を32bit整数に変換する関数を実装する。ただし以下の仕様がある。

1. 先頭の空白は無視する
2. 正負 (`-`, `+`) を判別する。符号が無い場合は `+`
3. 先頭のゼロは無視する。数字でない文字が出てくるか、終端まで読む。
   数字が全く登場しないときはゼロを返す
4. `[-2^31, 2^31-1]` の範囲に丸める

制約は `0 <= len(s) <= 200`.

仕様通りに処理していけば良さそう。

1. (a) 正規表現、(b) ポインタ、(c) `str.replace` が思い浮かぶ。(c) は先頭のだけを処理するのが難しそう。
   (a) よりは (b) のほうが読みやすいだろう。
2. 空文字でないことを調べた上で先頭の文字を見る。
3. 1. と同様に先頭のゼロを読み捨てる。その後、数字以外が出てくるまでの範囲を `int()` で変換する。
   これも正規表現とポインタが思い浮かぶが、同様に後者。
4. min, maxでroundingできる。if文よりはlower, upperそれぞれとmax, minを取るほうがすっきりしてそう。
   Pythonではオーバーフローを気にしなくて良さそう（少なくとも今回の値域では）。

時間計算量は `O(N)`. ただし `N = len(s)`.
空間計算量も `O(N)`. integerに変換するときにスライスができる。

大きく躓くところはなかったが、細かいミスをいくつかしてしまった。メモしておく。

* フラグ `is_minus` を付けてたのに処理忘れ。
* `num_end` を `num_last` と勘違い。対象外の文字を見たらbreakしていたので、最後にインクリメントしたインデックスの文字は対象外。
* leading zeroesを抜いた後に、`0` を受け付けるのを忘れていた。

## step 2

コードを整理する。
前問[31. Next Permutation](https://github.com/mamo3gr/arai60/pull/53) での学びを踏まえて、while文でインデックスを探している箇所をサブルーチン (inner function) に切り出す。

### 他の人のコード

#### https://github.com/h1rosaka/arai60/pull/58

1. では `str.lstrip()` が使えそう。  
https://docs.python.org/3/library/stdtypes.html#str.lstrip

`string.digits` というのがある。  
https://docs.python.org/3/library/string.html#string.digits  
これに対して `in` 判定するのも選択肢としてはある。
毎回10文字舐めるのか…？と思ったけど、N=200くらいなんだから気にしなくていいのかも。

整数への変換はこれが想定解だったのかも。`int()` は先頭のゼロを無視できるし便利すぎた。

```python
digit = ord(s[index]) - ord('0')
number = number * 10 + sign * digit
```

#### https://github.com/Satorien/LeetCode/pull/58

1. と 2. をまとめて処理しちゃう、という選択肢の幅もある。

https://github.com/Satorien/LeetCode/pull/58/changes#r2698302800

>他の(オーバーフローが)問題になるような言語だと、標準ライブラリーにそういう関数があることが多いというのも意識してもいいかもしれません。
>まあ、要は自分で作らないべきものであるということです。

どこでも困るから、何かしら対策手段がもうあることが多い、ということか。
ちょっと調べてみたら、例えばC++では、gccにビルトインのチェック関数があるようだ。  
https://gcc.gnu.org/onlinedocs/gcc-8.2.0/gcc/Integer-Overflow-Builtins.html

lower, upper boundは次のようにも書ける。が、Pythonなら `2**31` の方が可読性が高いように思う。

```python
MAX_INT = (1 << 31) - 1
MIN_INT = -(1 << 31)
```

#### https://github.com/naoto-iwase/leetcode/pull/60

正規表現で、先頭の空白、符号、数字を取ってしまうパターン (step1).

```python
whole_match = re.match("\s*([\+\-]?)([0-9]+)", s)
```

`int()` は符号もパースしてくれる。  
https://docs.python.org/3/library/functions.html#int  
もっと早くこのリファレンスを見に行くべきだった。

>Optionally, the string can be preceded by + or - (with no space in between), have leading zeros, be surrounded by whitespace, and have single underscores interspersed between digits.

後ろの空白、数字の間のアンダースコアは `int()` が無視してくれるが、
これらは今回の仕様では「区切り」になるので、自分で処理してから渡す必要がある。

`str.isdecimal()`, `str.isdigit()`, `str.isnumeric()` がある。  
https://docs.python.org/3/library/stdtypes.html#str.isdecimal  
上付き文字やアラビア文字、漢数字などにもヒットする・しないがある。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.j1ggirt9v3pc

#### https://github.com/katsukii/leetcode/pull/9#discussion_r1919816731

Javaには、オーバーフローしたら例外を投げてくれる関数 `multiplyExact`, `addExact` がある。

## step 3

実装済みの関数や機能に頼る。

leading zeroesは `int()` のパースに任せてよい。
符号もパースできるが、`-`（符号だけ、数字なし）のようなパターンを弾く必要があるので、
先に符号だけ自前で確定したあとで数字の範囲を探したほうが処理が楽そう。

Pythonなのでオーバーフロー対策は特に必要なし。
