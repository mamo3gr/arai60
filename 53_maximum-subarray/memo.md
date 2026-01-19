## step 1

整数の配列 `nums` が与えられたとき、総和が最大になるsubarrayを探し、その和を返す問題。  
配列の要素数 `N` は最大で10^5. 要素の値域は `[-10^4, 10^4]` である。

全く工夫のないbrute-forceとしては、`nums[i:j]` を `i = range(N)`, `j = range(i+1, N+1)` で総当たりする。ただし、これだと時間計算量が `O(N^3)` かかってしまう（i, j, subarrayの総和で3重）。  

過去に見たテクニックで使えそうなものを発想すると累積和かな。  
`c[i] = sum(nums[0:i+1])` とすると、`nums` を途中まで舐めたとき、  
`c[i]` と、`c[i] - c[j] for j in range(0, i)` が計算できる。  
maxを覚えておけば、`nums`を舐める・`j` を舐めるの `O(N^2)` でいけそう。  
ところで、`c[i] - c[j]` を最大にするなら `c[j]` は最小になっているはずで、  
ここまで最小の `c[j]` のみ覚えておけば良さそう。  
これで `j` を舐める必要はなくなって、`O(N)` でいけるのでは。

処理時間を見積もる。  
Pythonの処理能力を10^7 [steps/sec] とすると、10^5 / 10^7 = 10ミリ秒のオーダーを予想する。  
メモリ使用量については、最大と最小の `c[i]` を覚えておけばよさそう。intを2個分である。

## step 2

### 他の人のコード

#### https://github.com/naoto-iwase/leetcode/pull/37

>- アルゴリズムの選択  
>  - subarrayは連続しているので、貪欲的に解けそうだなと感じた。  
>  - 和が最大なsubarrayが、負の整数を跨いでいる場合が厄介。これを重点的に考察した。  
>  - そこまでの積み重ねのリターンが負の整数分差し引いても上回る場合、跨ぐ価値があると考察した。  
>  - 一般化して、nums[i]を第i世代の生涯収支とみなし、負になったら子供に相続させるのを取りやめるという例えがはまった。  
>  - この例えで、（相続分を含めた）財産が最大だった世代の財産を答えればよい。  

面白い考察。  
Kadaneのアルゴリズムというらしい。  
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

この解法の方が、自分の解法よりも値の更新回数が少ない（オーダーは一緒）。  
ちょっと変形したら辿り着けそう。自分の場合は、最終的な答えを以下のように更新している。

```python
max_cumulative_sum = max(
    max_cumulative_sum,
    cumulative_sum,                       # c[i]
    cumulative_sum - min_cumulative_sum,  # c[i] - min(c[j])
)
```

ここで、`c[j]` (`min_cumulative_sum`) を記録しなくてよいようにするにはどうするか？を考える。  
このmaxで `c[i] - min(c[j])` を比べる必要がなくなるのは、`c[j] >= 0` のとき（このとき、
`c[i]` でmaxを更新するかどうかだけを考えれば良い）。  
つまり、`c[i]` がマイナスにならなければ、`min(c[i])` を記録・更新するのは不要になる。  
これが「マイナスになったら`cumulative_sum`を0にリセット」につながるのか。

Geminiにも壁打ちしてもらったが、分かりやすい対比をもらった。

>Before: 「原点から計った高さ」と「過去最低の高さ」を両方記録して、その差を見る。  
>After: 「最低地点からの高さ」だけを記録する。もしマイナス（＝最低地点更新）になったら、そこを新たな 0 地点（スタート地点）とみなす。

#### https://github.com/nanae772/leetcode-arai60/pull/31

先程のPRでは「マイナスならリセット」だったが、「ここまでの累積に`num`を足す」か「新しく`num`から累積するか」を選ぶ、という考え方もできる。なるほどー。

```python
subarray_sum = max(subarray_sum + num, num)
```

#### https://github.com/garunitule/coding_practice/pull/32

これもmaxでリセットをかけるパターン。コードとしてはシンプルだが、何をしているのか結構考えないと分からない。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.qgjy53psjkn2

https://discord.com/channels/1084280443945353267/1206101582861697046/1208428345092734976

>素朴な解法から始めて、効率化 & コードを洗練させていくイメージですかね

>いや、たぶん、だいぶ違う感覚です。
>
>上で並べたのは、「下に行けば行くほど洗練されていて無条件に良い」などではなくて、だいたいこれくらいの幅を持って見ているということを伝えたかったからです。
>
>どうせ、1番上は思いついたけれども、価値のないものだと思って捨てたでしょう。そこがいかんのですよ。

ここの感覚がちょっと分からなかった。素朴な解法から幅は広げるけれども、素朴だからといって捨てずに平等に選ぶ、ということだろうか。

### フォローアップ：分割統治法

LeetCodeより

> Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

というので、分割統治法でもやってみる。

配列を真ん中から割って、それぞれの答え（subarrayの和）を求めるのはできる。  
あと考慮すべきは、マージするときに、真ん中をまたぐときの和をどう求めるか、だ。

Geminiに手伝いながらやった。真ん中からスタートして、左に伸ばしたときの最大と、右に伸ばしたときの最大をそれぞれ求める。で、最後にそれら2つの合計を返す。

## step 3

https://github.com/naoto-iwase/leetcode/pull/37 の「マイナスなら相続をやめる」という考えがしっくりきた。
