## step 1

整数の配列が与えられ、最長のincreasing subsequence (LIS: Longest Increasing Subsequence) の長さを返す問題。  
subsequenceはsubarrayではない。配列のつまみ食いでよい。つまり、順番を変えなければ途中の要素をスキップしてもよい。

解法をちょっと考えてみる。  
シンプルには、ある要素から始まるLISは、その要素以降で、値がより大きい要素を拾っていけばいい。あーでも、拾うかどうかの選択があるな。先に大きい数字を拾ってしまうと、後で拾える要素が少なくなってしまう。

よく考えてみると、与えられた数列の頭から見て、要素を拾うかどうかを判断するとき、ある要素を拾うと、それ以降のLISは決まっている。  
`nums[i:]` から始めるIS (increasing subsequence) を考えたとき、その長さを `seq(i)` とする。
この配列の先頭に要素を一つ足した `nums[i-1:]` に対してISを考えると、

* `nums[i-1] < nums[i]` なら `seq(i-1) = seq(i) + 1`
* そうでないなら `1` である。

`seq(i)` は配列の後ろの`i=N-1`から決まっていくほうが簡単そう。`seq(N-1)=1` なのは自明であるから、残りの `N-2, ..., 0` に対して、

* seq(i) = max of
  * seq(j) + 1, where i < j and nums[i] < nums[j]
  * 1

を埋めていけば良い。

処理時間を見積もる。配列の長さを `N` とすると、`for each i in range(N)` で `seq(i)` を求めるし、さらにその中のループで `for j in range(i+1, N)` を回すので、`O(N^2)`. `N` は最大2500なので、Pythonの処理能力を10^7 steps/sec とすると、2500 x 2500 / 10^7 = 0.625秒くらいのオーダーを予想する。  
メモリ使用量は `O(N)`. というのも、`seq(i)` を `N` 個分だけ持つからである。28 bytes * 70 KBのオーダーを予想する。

あと、現時点で見える幅を書いておく。  
大きな方針として、`seq(i)` を頭 (i=0) から求めようとする、というパターンが思い浮かぶ。これは帰りがけの再帰になり、結局 `seq(N-1)` から求められることになる。前述のアルゴリズムも十分読みやすいと思うので、再帰にするメリットも特に無さそうだ。
細かい点では、`seq(i)` のdictを作っておくが、最後に `max(seq.values())` するのと、毎回maxを求める、の2択がある。書いてみた感じ後者でもそのまで複雑にはならない。

## step 2

### 他の人のコード

#### https://github.com/naoto-iwase/leetcode/pull/36

>`nums`を線形に走査し、次の要素`num`をこれまで作ってきた部分列のうち、一番長くなるものにくっつける。  
>なので、部分列の情報としては一番最後の要素と長さだけ覚えていればいい。  
>くっつけられるものがない場合は`num`から始まる新しい部分列を作る。  
>`nums`の走査が終わったら、一番長い部分列の長さを返す。  

思いつかなかった解法。自分でも書いてみる。  
書いてみて分かったが、step 1での解法に対し、頭から見ていくバージョンだった。

>- > tails配列（“長さLの増加列の末尾最小値”を保持）＋二分探索への置換で O(n log n) を狙える。  
>  - あーなるほど。理解しました。

理解できたの！？賢すぎる。  
コードを読みながら考えてみる。`tails: list` は、例えば `tails[2]` が、（ここまで分かっている）長さ2のISの、末尾の数字を示している。ただし正確には、元コードでは `tails[i]` が長さ `i+1` のISに対応するので、自分で書くときにはここを揃えるようにしたい。番兵みたいなのを置く（これもそう呼んでいいのだろうか？）  
`tails` もまた単調増加しているので、`for n in nums` に対して、`tails` の中のどこに入るかを二分探索で求められる。なるほどー。  
自分でも書けた！

https://github.com/naoto-iwase/leetcode/pull/36/changes#r2468874655

>自分なら length_to_min_tail または length_to_min_last_num とすると思います。コメントが書かれているので、 min_tails でも十分伝わると思います。

`tails` 変数の命名。

#### https://github.com/nanae772/leetcode-arai60/pull/30

max内に内包表記で `seq(j)` を書いちゃうパターン (step2-dp).  
こっちのほうが定式化をそのまま表せているが、ちょっと読むのに苦労する。

maxの引数 `default` 知らなかった。渡したiterableが空ならこれが返る。  
https://docs.python.org/3.13/library/functions.html#max

#### https://github.com/garunitule/coding_practice/pull/31

`seq(i)` を `[1] * N` で初期化したリストで持つパターン。たしかに、dictである必要はない。listの方が変更も参照も（このユースケースでは）速い。  

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.92aluhxkunm1

>うーん、読みにくいと思ったんですが、理由が  
>lengths  
>の意味がパズルになっているからだと思いました。
>
>日本語で長々と書くと、「lengths[i] とは、仮に nums[i] がシーケンスの最後であると仮定した場合に可能な、最も長いシーケンスの長さ」ですよね。
>
>まあ、「長さ(複数)」であることには間違いないですが、「長さ」とだけいわれて、ああ「仮に nums[i] がシーケンスの最後であると仮定した場合に可能な、最も長いシーケンスの長さ」ってことね、とならず、それを推測するパズルになっています。

パズルを作らない。なるほど。

解法が結構あるらしい。  
https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/

1. Dynamic Programming: Let `dp[i]` be the longest increase subsequence of `nums[0..i]` which has `nums[i]` as the end element of the subsequence.
  - step1, あるいはその頭から見ていくバージョン
2. Greedy with Binary Search
  - さっきやった、二分探索のやつ
3. Binary Indexed Tree (Increase BASE of nums into one-base indexing)
4. Binary Indexed Tree (Compress nums into values in [1...N])
5. Segment Tree

BIT (Binary Indexed Tree) とSegment Treeが分からないので読んでいく。

https://discord.com/channels/1084280443945353267/1206101582861697046/1209027377397506109

>オープンワールドのゲームの RTA みたいな感じを受けていますが、大事なのは、
>見たときに大局的に色々な手段が見えていること。  
>その中には遅いものも速いものもあり、色々な良し悪しで評価できること。例えば速度の見積もりとかもそれ。  
>それぞれの手段の間の移り変わりの関係性が見えていること。  
>局所的に変更して、見やすくしたり、整理したりすることができること。  
>
>だいたい、この辺です。

そもそも、まだ「色々な手段が見えていること」ができてない。  
解いているうちに引き出しが増えていくのかな。

https://github.com/naoto-iwase/leetcode/pull/36/changes#r2468854052

>セグメント木はソフトウェアエンジニアの常識には含まれていないと思います。

>セグメントツリーは、50行以内で書け、いろいろな複雑なデータ構造の代用品として使えるので重宝されます。

常識ではないが便利、ということらしい。

### Segment Tree

`nums` の値域に対し、整数と一対一対応したノードを持つ、完全平衡二分木を考える。  
葉のノードには、そのノードに対応する整数 `X` について「`X` 以下の要素だけを含むLISの長さ」＝「末尾が `X` のLISの長さ」を格納するようにする。  
また、親のノードでは、接続している子のmaxを取っている（トーナメント表のイメージ）。  
`nums` を舐めて、この木を更新していく。

ノードに対応するクラスを定義してもいいが、完全平衡二分木なのでlistでも管理が容易である（親-子のインデックスは2倍の関係）。  
`update(index, value)` では、indexから葉ノードの位置を特定して値を更新する。その後、親ノードを遡っていき、同様に値を更新する。

クエリでは、区間の開始・終了を指定し、この間でのLISの最大値を得られる。最大値の探索では、クエリ区間をカバーする葉ノードと親ノードの組み合わせの中でのみ最大値を取れば良い。

あと、座標圧縮というテクニックがある。本問では `-10^4 <= nums[i] <= 10^4` という値域だったが、これに対応するsegment treeのノード数は20000個になる。一方で`nums`には必ずしもすべての整数が登場するわけではないので、無駄なメモリを確保している場合がある（木がスカスカ）。  
そこで、`nums`の要素を、要素内のランク（ソートしたときの座標）に置き換えることを考える。例えば `[1, 9999, 20, 10, 20]` を `[1, 4, 3, 2, 3]` と変換する（ここでは1-indexにしている）。後者の配列に対して解いても同値になる（！）。

LeetCodeのSolutionsや https://github.com/naoto-iwase/leetcode/pull/36 を書き写す形で書いてみて、何とか動いた。木→配列のイメージがまだあやふやなので、後で再訪したい。

## TODO

- [ ] セグメント木を自力で書けるようにする
- [ ] Binary Indexed Treeを調べる
