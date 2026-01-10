## step 1

[200. Number of Islands](https://leetcode.com/problems/number-of-islands/) と同様の設定で、今度は面積の最大を求める。  
200. の変形で解けそう。未踏の島から隣接する島への探索を始めたら、その終了時に島の数をカウントしたらよい。

## step 2

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/pull/23

島のトラバースをする関数 (`calculate_area_of_island`) を関数の中で定義している。この形は関数の外側への変数にもアクセスできる一方で、どれに依存するのかわかりにくくなってしまうので、自分としてはなるべく避けたい気持ちがある。一段インデントが上がるのも可読性を下げる。

DSU (Union-Find) による解法あり。この機会に自分もやってみるか。

https://github.com/Shoichifunyu/shofun/pull/13

未踏の島なのかを返す関数 `is_frontier` なるほどね。ちょっと frontier という単語に多くの情報を伝えることを期待しすぎなきらいはある。

* 眺めたが、前述のPR, あるいは前問 (200. Number of Islands) で得られた知見のみだった。
  * https://github.com/docto-rin/leetcode/pull/18
  * https://github.com/nanae772/leetcode-arai60/pull/19

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.f28i04p206ak

https://github.com/Fuminiton/LeetCode/pull/18#discussion_r1986038739

>私は、これを書き下すかもしれませんね。  
>visiting.append((current_r, current_c + 1))  
>visiting.append((current_r, current_c - 1))  
>visiting.append((current_r + 1, current_c))  
>visiting.append((current_r - 1, current_c))  
>まとまっていたほうが読みやすいと思うからですが。まあ、趣味の範囲です。

ベタに書き下すパターンもある。

### UnionFindの実装

https://github.com/Yuto729/LeetCode_arai60/pull/23 を参考にUnionFindを実装してみる。

- `UnionFind` クラスを定義する。コンストラクタで次を初期化する。
  - それぞれの島が所属するグループの番号：はじめはすべての島が異なるグループに所属する
  - グループごとの島の面積
  - `grid` は2次元だが、こちらは1次元で持つのが扱う上では楽そう。でも島だけをスパースに扱うなら2次元も捨てがたい
- 2つのメソッドを実装する。
  - `find(x)`: xが属するグループを特定する。より正確には、グループとは島をノードにした有向グラフで、その親のノードを特定する。
  - `union(x, y)`: xとyをマージして同じグループにする。本問では、面積も足し合わせる。
- それぞれの島について、右と下の隣接する島に対してunionしていく。
- unionでのマージでは、適当にやっていると最悪のケースで長いlinked listができてしまう。
  - https://zenn.dev/convers39/articles/ffd666639e7782#unionのランク付
  - マージ時に、なんらかの優先順序を付けると回避できる。本問では面積が良さそう。
- 経路圧縮 (Path compression) というテクニックがある。
  - https://zenn.dev/convers39/articles/ffd666639e7782#path-compression
  - 素朴な実装のfindでは順に親を辿っていくため、何回もfindを呼び出す必要がある。`O(log n)`.
    再帰の呼び出し中に最終的な親に付け替えることができる

実装してみての所感

- 全部海の場合（エッジケース）を避けるために、島の面積を1で初期化できない。島であるノードだけ1を代入するという手間がある。
- 最後にareaのmaxを取る必要があるのが手間。まあもともと `O(M x N)` かかっているので、このオーダーを変えるわけではないのだが…。
  - unionのたびに統合後のareaを返り値で受け取ることもできるが、メソッドの名前よりも多くのことをしているので避けたい。
- `UnionFind` という名前は改善の余地がないか。アルゴリズムを表しているのでまあいいか…。

## step 3

一度にメモリに乗らないほどグリッドが大きい、というのでなければ、DFSの解法の方が書きやすい・読みやすい・メンテナンス性も高そう。

