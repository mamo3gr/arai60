## step 1

前問である[Unique Paths](https://leetcode.com/problems/unique-paths/)に、障害物が追加された問題。

解法の方針としては、反復法で `f(m=0, n=0) = 1` から、過去の結果のうち左・上を足し込むことで計算していけそう。  
障害物をどう考えるか。障害物があるマスからスタートする経路はすべて通れないので、`f(m, n) = 0` として良さそう。  
端の処理（初期化）もちょっと変わる。前問では、一行あるいは一列のみのグリッドなら必ず1通りになった。例えば `f(m=5, n=1) = 1`. 今回は、その間に障害物があるとコールできなくなる（つまり `= 0`）。

まずは二次元配列で書いてみる。step 2で一次元配列へ変形を試みる。  
時間計算量は、`O(m x n)`. 制約より `m`, `n` はそれぞれ最大100で、Pythonの処理能力を 10^7 steps/sec とすると、100 x 100 / 10^7 = 10ミリ秒くらいのオーダーを予想する。  
空間計算量も同様。反復法に使うグリッドとして 100 x 100 x 28 bytes = 280 KBくらいを予想する。

## step 2

col=0のときは上からだけ足し込む、とすることで1次元配列にできた。

### 他の人のコード

#### https://github.com/naoto-iwase/leetcode/pull/39

1次元配列での反復法。自分の場合はrow=0の行で初期化していたけど、これもメインループに組み込める。

メインループ。`col == 0` でcontinueというより、前の列を引き継いでそのまま、って感じにするとより分かりやすいと思う。

```python
        for row in range(num_rows):
            for col in range(num_cols):
                if obstacleGrid[row][col] == 1:
                    count[col] = 0
                    continue
                if col == 0:
                    continue
                count[col] += count[col - 1]
```

再帰+メモ化での実装もある。後で自分もやってみよう。  
メモ化には `functools.lru_cache` を使う、と覚えていたのだが、`functools.lru_cache(maxsize=None)` と同様に使える `cache` というのもある。   
https://docs.python.org/3.13/library/functools.html#functools.cache

#### https://github.com/nanae772/leetcode-arai60/pull/33

`OBSTACLE = 1` と置くのは丁寧だ。

二重ループを `itertools.product` で書くと、インデントが一つ下げられる。

#### https://github.com/garunitule/coding_practice/pull/34

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.qdbwc4eyd7p0

https://github.com/olsen-blue/Arai60/pull/34/changes/BASE..906129e40bb86e778eb69733ffb9bd497504f664#r1968666138

>コードを書くというのはすべて地雷の埋設(使われなくなるまでに爆発しなければ勝ち)くらいに思っておくといいでしょう。作る時にだいたいどれくらいで爆発するか見積もります。また、壊れるにしても安全に壊れて欲しいです。ユーザーに届く前に事前に気がつくとか不完全ながらも結果は返るとか止まって異常があったことが分かるとか何がいいかは状況次第です。

### 再帰+メモ化

メモ化するヘルパー関数の命名に悩む。`_recursive` くらいしか情報を載せられなさそうだが、それも中身を読めば分かる。`helper` よりはマシかなあと思い親関数の一部である `unique_paths` にしておく。

再帰関数の中身。条件分岐のやり方はあるが、障害物があったら0, 原点なら1, とearly returnするのが好み（毎回原点かどうかのチェックが入るのはちょっと冗長な気もするが）。あとは、上の行があるなら引き継ぐ、左があるなら引き継ぐ、という書き方がしっくりくる。

## step 3

1次元配列を用いた反復法をもう一度書く。  
`0:m`, `0:n` でループを回そうとすると、`unique_paths = [1, 0, ..., 0]` という初期化が必要。左端の1は原点に障害物がなければそう決まる。それ以外の0は「上の行からは引き継がない（左からのみ貰う）」というつもりのゼロで、そうするとまあうまく動く、というように感じられる。  
それなら1行目を意図を持って初期化して、`1:m`, `0:n` でループを回すほうが自然に感じた。

