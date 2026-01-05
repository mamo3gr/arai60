## step 1

`beginWord` から「1字だけを変更する」処理を繰り返して、`endWord` を目指す。辞書 `wordList` に含まれる単語のみを経由する。最短の変更数を調べる。単語長は最大10文字、辞書の語数は最大5000語。

まず思いついたのは、「現在の単語」と「`wordList` 内の使っていない単語」（とホップ数）をステートとして、1文字だけの変更の関係にある＝隣接した単語を幅優先探索していく、という方法。  
単語長を`L`, 辞書の語数を`W`とすると、ある2つの単語が隣接するか（相互に変換可能か）調べるには、時間計算量と空間計算量が `O(L)` かかる。  
現在のステートから遷移できるステートを列挙する時間計算量は、最悪ケースとしてすべてのステートが直列である場合を考えると `O(W^2)`. つまり全体で `O(L x W^2)`.  
空間計算量が大きそう。ステートあたり、(1) 単語 (str) ひとつと (2) `W` 個の文字列、(3) ホップ数 (int) を保持することになる。(2) が支配的なのでこれだけ考えることにすると、辞書へのインデックス (int) を持つとしても、ステートひとつで5000個のint, つまり5000 x 28 bytes/int = 0.14 MBかかる。すべてのステートが幅優先探索の1階層に含まれるとすると `O(W^2)`. 0.14 * 5000 = 700MB くらいかかる。現代の計算機のメモリに載らないことはないがもっと削減できそう。ちなみにダメ元で実装してみたがMemory Limits Exceededだった。

「`wordList` 内の使っていない単語」x ステート数がネック。ステートごとに残りの単語を保持しなくても処理可能ではないか。単語をノード、隣接する単語の間をエッジとすると、最短経路問題に帰着できることを発想する＝Dijkstra法で解ける。エッジの長さはすべて1なので、スタートのノードに隣接するノードを起点として（ホップ数=1）、いずれかのノードに隣接するノードを列挙してホップ数=2をセット、今度はそれらのノードを起点に隣接するノードを探す…としていけばよい。これだと時間計算量は前述の解法と変わらないものの、空間計算量は `O(W)` にできる。すなわち、起点にするノードのインデックスを保持するのに高々 `W` 個のintと、ノードごとにホップ数を記録する長さ `W` の配列である。  
ちなみに、反対に `endWord` から探索を始めてみた。というのも、`wordList` に `endWord` が含まれない場合は探索なしに結果を返せるし、本処理のループを書くうえで `wordList` に入っている単語を起点にできるのでコードが比較的スッキリすると考えたからだ（`beginWord`は`wordList`に含まれない）。

コードはあんまりまとまっていないが、何とかテストをパス。ちゃんと考えてパスまでたどり着けたのはちょっと達成感がある（とはいえこの練習としてはこれで3割程度の達成率）。

## step 2

本問では各単語への距離は不要なので、`word_to_hops: list` ではなく未使用の単語だけを入れた `word_list: set` を使うことにした。こちらもlistにするか迷ったが、`for word in word_list` のループ中に `.remove(word)` メソッドで単語を取り除けないので、ループを抜けた後に `used_list: set` との差集合で取り除くようにした。  
コードはすっきりしたがRuntimeはさほど変わらず。他の人の解法や書きぶりを参照する。

### 他の人のコード

#### https://github.com/Yuto729/LeetCode_arai60/pull/25

隣接する単語を調べるためのクラスを定義している。こんな感じ。

```python
class WordNeighbors():
    def __init__(self):
        self.pattern_to_words = defaultdict(list)

    def to_key(self, word):
        for i in range(len(word)):
            yield (word[:i], word[i+1:])

    def add_word(self, word):
        for key in self.to_key(word):
            self.pattern_to_words[key].append(word)
    
    def get_neighbors(self, word):
        for key in self.to_key(word):
            for w in self.pattern_to_words[key]:
                yield w
```

`add_word` と `get_neighbors` は分かりやすいが（命名に感謝）、`pattern_to_words` と `to_key` が何をしているのかパッとは分からない。メソッド `to_key` は、例えば `dog` を与えると `(, og)`, `(d, g)`, `(do, )` が yieldされる。`add_word` では、これらのタプルをkey, もとの単語をvalueとして辞書 `pattern_to_words` を作る。そうすると、例えば隣接する `dig` は `(, ig)`, `(d, g)`, `(di, )` になり、共通のkeyを持つので `get_neighbors` で引ける。なるほどね。

訪問済みかどうかは set で管理している。

先にすべての単語間の隣接を調べてしまう、というのは半ば無意識に外してしまっていた。記憶するために `W^2` の空間が必要なのと、通らない単語が存在する＝無駄な計算をしてしまう可能性を発想したため。

#### https://github.com/plushn/SWE-Arai60/pull/20

https://github.com/plushn/SWE-Arai60/pull/20/files#r2588357494

>自分なら BFS の未探索領域の意味で、 frontier と名付けると思います。

frontier, 聞き慣れなかったがメジャーなのかな。

双方向でBFSをやる、という方法もある。`beginWord` から `front_layer`, `endWord` から `back_layer` を進めていく。深さが小さい方を `front_layer` になるようにスワップして、そこに新しい深さを足す。  
実装は複雑だけど、片方向の1/2の深さで解にたどり着くので、探索の幅が狭く速度も優れる（Geminiに聞いた）。

https://github.com/plushn/SWE-Arai60/pull/20/files#r2623544663

>引数もスネークケースに統一した方がよいかなと思いました。

勝手に引数は変えてはいけない、と思い込んでいたが、順番さえ保持していれば変更して良さそう（位置引数）。でもキーワード引数で呼び出される場合もあるよなあ。

#### https://github.com/yas-2023/leetcode_arai60/pull/20

前述の `WordNeighbors` クラスでは `dog -> (, og), (d, g), (do, )` のような1文字抜きのタプルを作ったが、`dog -> *og, d*g, do*` というワイルドカード入りの文字列としても表現できる。

自分の実装では、現在の深さの単語と、次に探索する深さの単語をそれぞれキュー（正確にはlist）に入れて、ループが終わるたびにスワップしていた。このコードでは、`(単語, 深さ=距離)` のタプルをキューに入れている。こうすると、ある深さごとの探索が終わったかどうかを気にする必要がなくなる。

#### https://github.com/docto-rin/leetcode/pull/19

https://github.com/docto-rin/leetcode/pull/19/files#r2428448628

>countについてはむしろ、layer-wiseの方がインクリメントの位置が直感的

深さごとのループのメリット。

#### https://github.com/nanae772/leetcode-arai60/pull/20

隣接グラフとして、`wordList` のインデックス `i` から隣接する単語群へのインデックス (list) を持つ、2次元配列を用意している。この配列は `O(W^2)` の空間が必要だが、隣接する単語を `O(1)` で引ける。

### コメント集

https://github.com/goto-untrapped/Arai60/pull/57#discussion_r1781365485

>とりあえず、前計算と本計算は、関数で分離してみましょう。そうすると別にテストができるはずです。
>
>つまり、何かをしようとして、そのことを覚えておきながら別のことをしようとすると、覚えておかないといけないので混乱するんですよね。

関数の切り分けは（やりすぎるくらい）好きなので、この辺はできていそう。

https://github.com/shining-ai/leetcode/pull/20/files#r1517022719

>transformation_numって命名間違っていると思うんですよね。
>
>hot -> dot -> dogとすると、transformationはそれぞれhot -> dotとdot -> dogの2だと思いますが、今回求めたいのはhot, dot, dogなので3になります。

自分の `num_hops` も同様に間違っている気がする。
