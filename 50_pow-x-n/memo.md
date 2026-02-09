## step 1

`pow(x, n)` を実装しろ、という問題。制約は次の通り。

* -100.0 < x < 100.0
* -2^31 <= n <= 2^31-1
* n is an integer.
* Either x is not zero or n > 0.
* -10^4 <= x^n <= 10^4

`x` と 答え `x^n` の範囲は比較的狭いものの、`n` が大きい。
つまり、定義通り `x` を `n` 回掛け算する、では時間がかかりすぎるだろう。

階乗の性質を使って簡単な計算に帰着することを考える。
例えば 2^10 = 2^5 * 2^5 のように、x^n = x^{(n/2) * 2} に分解できる。
さらに 2^5 = 2^2 * 2^2,
2^2 = 2^1 * 2^1 と分解できる。
2^5 のように、nが奇数のときは、2^(4+1) = 2^2 * 2^2 * 2^1 というように、n/2, n/2, 1に分解できる。
あとはこれをcacheしつつ再帰すれば良い。
再帰で書けるということはループでも書けるということだが、再帰の方が書きやすそうなので、まずはこっちで。
`n` は最大2^31 - 1 ということで、再帰の深さはlog2(2^31) = 31だから、Python標準の上限1000を超すことはなさそう。

処理時間を見積もる。
素朴な方法では `O(n)` で、Pythonの処理能力を10^7 steps/sec とすると、
2^31 / 10^7 = 214秒くらいのオーダー。たぶんTLEするだろう。
前述した分解＆再帰だと、`O(log n)` になる。log2(2^31) / 10^7 = 3マイクロ秒くらいのオーダーを予想する。  
メモリ使用量については、再帰の深さが `O(log n)` になる。今回の制約からlog2(2^31) = 31.
再帰あたりフレームオブジェクトを150 bytesとすると、150 * 31 = 4.6KBくらいのオーダーを予想する。

あと、`n` が負のときの処理もちょっと考える必要がある。
先に `x` の逆数を取るよりは、`x` の階乗を計算したあとで最後に逆数を取ったほうが、
コードの見通しが良さそう。毎回浮動小数点の除算が発生しないのも計算コストの観点から良い。

## step 2

Geminiにレビューしてもらった。

* `pow` は組み込み関数をシャドーイングしてしまう
  * https://docs.python.org/3.13/library/functions.html#pow
* 再帰呼び出しの結果を変数に束縛すれば、`functools.cache` は不要

なるほど。

### 他の人のコード

#### https://github.com/h1rosaka/arai60/pull/47

whileループで、x^2, x^4, x^8, ... と x^n乗になるまで2乗していくパターン (step1).
`list[tuple[int, float]]` に、y乗したときの結果x^yをappendしておき、
yがnを飛び越すなら、これまで計算した中で飛び越さないyまで戻る。

#### https://github.com/hayashi-ay/leetcode/pull/41

前述のPRからリンクを辿って読む。

再帰 (step1). 2^4 -> 4^2のように、乗数yを底xに入れ込んでいくイメージ。

left to right binary exponentation (step 2).
nを2進数表記し、xを2乗しながら、1が立っている桁だけかけていく。
例えば3^13を計算するとして、13 = 1101(2) だから、
3^13 = (1 * 3^8) * (1 * 3^4) * (0 * 3^2) * (1 * 3^1) と分解できる。
nを2で割った余りが最下位ビット。nを右にビットシフトしながら2で割った余りを見ることで、
各桁に1が立っているか調べられる。
元のPRではleft to rightと書いているが、見ている桁からするとright to leftに思える（リトルエンディアン？）。

left to rightというのもあるらしい。

>Pythonのpowはこの方法。数が多いときはk-ary sliding windowでwindowサイズずつ計算していく。

left to rightでは、2進数表記したnを最上位ビットから見ていく。
ビットが0だろうが1だろうがxを2乗し、その後、1だったらさらにxをかける。
例えば3^13なら、13 = 1101(2) だから、3^1から始めて、
2乗して3^2. 左から2番目のビットも1だから、さらに3をかけて3^3.
2乗して3^6. 左から3番目のビットは0だから、そのまま。
2乗して3^12. 左から4番目のビットは1だから、さらに3をかけて3^13.

`(n >> i) & 1` のようなビット演算が急に出てくると、個人的にはびっくりする
（特にPythonなどの比較的高水準な言語では）。
変数名やコメントで補ったほうが分かりやすそうだが、これくらいは常識なのかな。

#### https://github.com/h1rosaka/arai60/pull/47

戻ってきた。

ビットごとではなく、ある程度のまとまりで処理する方法もある (sliding window).

>- sliding windowでの計算イメージ
>    - あらかじめ、x¹, x³, x⁵, x⁷を作っておき、下記計算。
>    ```
>    11  → x³ を1回で掛ける
>    0   → 平方だけ
>    101 → x⁵ を1回で掛ける
>    01  → x¹ を掛ける
>    ```
>    - 例えば、最初の2桁は、二分累乗だと、xかけて、それに2乗してxかけてx^2になって、その後次の桁のxを掛けるので、結局x^3になる。
>    →だったら最初からx^3を掛けよう。
>    - ウィンドウのルール
>        - 左のビットから見ていく
>        - 次のビットが 0 の間は window を作らない（平方だけ）
>        - 1 を見つけたら window 開始
>        - 最大 k ビットまで、かつ「最後が 1 になるように」window を伸ばす(上の例はk=3)
>        - 作ったウィンドウを1回の掛け算で処理
>    - 最後が1になるようにwindow作るので、あらかじめ用意する累乗結果は奇数だけでOK。

#### https://github.com/garunitule/coding_practice/pull/45

right to left binary exponentation (step3).
`bit = 1` として、これと `n` のビット論理積を取ることで、各桁のビットを見ている。
`bit <<= 1` のように左にシフトしていくので、見るビットをずらしていける。

#### https://github.com/naoto-iwase/leetcode/pull/46

https://github.com/naoto-iwase/leetcode/pull/46/changes#r2476480035

>absで回さずに、if n < 0: return 1 / myPow(x, -n)を最初の方に持ってきてここにくる段階ではn > 0の時を考えれば良いようにした方が見やすくなる気がしました。

さっさと同じルーチンにのせてしまう、なるほど。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.d9ky6ipkmw98

https://github.com/hroc135/leetcode/pull/43#discussion_r2651608999

>0^0 は 1 のほうが自然に感じますね。
>空集合から空集合への射の数と考えるからです。

https://github.com/TORUS0818/leetcode/pull/47#discussion_r2031692691

>こっちは、n を破壊しているために関係が見にくくなっているのだろうと思います。

前述のように、見る `bit` を動かしていったほうが賢い。

https://github.com/TORUS0818/leetcode/pull/47#discussion_r2038331269

>が、まあ、しかし、「上のビットから回している」「全体を自乗すると指数が倍になる」がどちらにしても分かりにくいと思います。

ここは感覚が一緒で安心。

## step 3

ビット演算のケースでimplicit falseは使えるのか？Googleのスタイルガイドを読み直す。 
https://google.github.io/styleguide/pyguide.html#2144-decision

>When handling integers, implicit false may involve more risk than benefit (i.e., accidentally handling None as 0). You may compare a value which is known to be an integer (and is not the result of len()) against the integer 0.

今回のケースは2文目に当てはまりそう。ビット演算しているので整数のはずで、
`None` など想定外の型の変数が紛れ込んだらTypeErrorが送出される。

