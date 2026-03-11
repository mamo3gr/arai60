## step 1

会議時間の区間を表すオブジェクト `Interval` の配列が与えられたとき、重複があるかどうかを返す。
`Interval.start` と `Interval.end` は半開区間である。つまり `[start, end)` で、
`[(0,8), (8,10)]` は重複しない。制約としては

* 0 <= `intervals.length` <= 500
* 0 <= `intervals[i].start` < `intervals[i].end` <= 1,000,000

最もシンプルにやるには、`intervals[i]` を `intervals[j]` と順番に比べていくことが思いつく。
これだと `N = intervals.length` とするとき、`O(N^2)` かかる。
`N` は最大500で、Pythonの処理能力を10^7 steps/sec とすると、
500 * 500 / 10^7 = 25ミリ秒くらいのオーダーで終わる。
これでもいける気がするが、他の選択肢も考えてみる。

ところで、重複がないとき、`intervals` をソートすると、
`(start, end), (start, end), ...` が単調増加になる（`end=start`も許容されることに注意）。
これなら時間計算量 `O(N logN)` で解けそう。補助空間として `O(N)` 必要になる。
500 * log2(500) / 10^7 = 0.5ミリ秒くらいのオーダーになる。
補助空間は 28 bytes/int * 2 * 500 = 28KB くらいのオーダー。

ソートのキーは`start`だけで十分だろうか。`[(0,1), (0,20)]` の場合を考えてみると、
どちらが先に来たとしても重複を検知できそう。
`sorted()` はたぶん安定ソートだろうと思って念の為してみた。  
https://docs.python.org/3/library/functions.html#sorted
結論として `start` をキーとしてソート、で良さそう。
そして `end` も何か追加の用途で使いたいなら、キーをタプルにしちゃえばいい。

## step 2

隣接する要素をインデックスで取りに行っているが、`itertools` に同様の処理がありそう。-> あった。  
https://docs.python.org/3/library/itertools.html#itertools.pairwise

### 他の人のコード

#### https://github.com/Satorien/LeetCode/pull/54

`[FREE for _ in range(1,000,000)]` のスケジュール配列に対し、`BOOKED` を埋めていくパターン (step1).
スケジュールの分解能と最大長によってはこれでも解ける。なるほどー。

step2は、自分のstep1と同様にソートして前後比較。

#### https://github.com/shintaro1993/arai60/pull/59

ソートして前後比較するのは同様だが(step2), `end = last_end_time` として、ループの次の `start` と比べると、
隣接する要素を取り出すのではなく、`for inteval in intervals` のループで書ける。

#### https://github.com/olsen-blue/Arai60/pull/56

累積和の問題と考えて解く (step1).
`schedule = [0 for _ in range(1,000,000+1)]` を用意しておいて、
for each intervalに対し `schedule[start] += 1`, `schedule[end] -= 1` とする。
最後に `schedule` の累積和を取ると、重複が発生する時間帯では1を超える。
つまり時間帯ごとに必要な会議室の数を求めているということか。

データ構造としてはかなり疎なので、変化がある点だけ覚えておくというアレンジもできそう。

https://github.com/olsen-blue/Arai60/pull/56/changes#r2023904388

>座標圧縮みたいなことをする手はありますね。

言われてた。

もとの解法を差分配列 (difference array) というらしい。

#### https://github.com/hayashi-ay/leetcode/pull/59

heapを使う手もある (step2).
この問題ではソートを使うのが概ね有利そう。
何らか途中で会議が追加されるときには、heapでは `O(log N)` で追加できる。

`heapq` は扱うオブジェクトに `__lt__` の定義が必要らしいが、
https://github.com/Satorien/LeetCode/pull/54 では自作の関数を割り当てていた。

### コメント集

発展問題の "Meeting Rooms II" の見出しはあるが、本問のものは見つからなかった。

### パターンをいくつか

step1でやってない解法を自分でも書いてみる。

## step 3

座標圧縮に近い考え方で、必要な会議室数の増減タイミング（イベント）を集めてソートし、累積してチェック、
というのが応用も広そう。デメリットはtwo-passになること。
ChatGPT曰く、このアプローチはsweep lineというらしい。
`all()`, `itertools.accumulate()` を使ったイディオムより、forで累積するほうが読みやすそう。
