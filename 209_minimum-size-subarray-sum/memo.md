## step 1

正の整数からなる配列 `nums` の中から、和が `target` 以上になるsubarrayについて、
長さの最小値を求める。見つからない場合は `0` を返す。制約は次のとおり。

* 1 <= target <= 10^9
* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^4

`len(nums)` （以降 `N` とする）が10^5なので、`O(N^2)` のように2重に走査するとTLEしそう。
最終的には一度の走査で完了するアルゴリズムを考えないといけない。

とはいえ、最初は素朴に考えてみる。subarrayは `start` と `last` が決まれば一意に定まる。
`for start in range(len(nums))`, `for last in range(start, len(nums)` という
2重ループにする。`subarray = nums[start:last+1]` の和を計算し、
`target` 以上か、そうであれば `min_length` を更新すればよい。

計算を省略する方法を考える。
`i` を固定し、`j` を延ばしていったとき、`nums[i:j+1]` が条件を満たした（`target`以上になった）とする。
このとき、`nums[i]` を引けば、`nums[i+1:j+1]` から探索を継続できる。

* `target` 以上になるまで、`last` を進める
* `min_length` を更新する
* `target` 未満になるまで、`start` を進める

という感じで書けそう。

これで時間計算量が `O(N)` になった。Pythonの処理能力を 10^7 steps/sec とすると、
処理時間は 10^5 / 10^7 = 10ミリ秒くらいのオーダーを予想する。
空間計算量は `O(1)`. 具体的には、`start`, `last`, 現在の合計 `total`, `min_length` くらい。
4 * 28 bytes/int = 112 bytesくらいのオーダーを予想する。

`min_length` の更新タイミングや、`start`, `last` の進め方で苦労したが、何とかパス。

## step 2

前問 [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) を思い出すと、`last` を増やすループを軸にして、条件を満たしていれば `start` を進める、とすると整理できそう (step2_1.py).

ここからさらにGeminiの力を借りて整理する (step2_2.py). 指摘点は次のとおり。

* `min_length` を配列の長さより大きい値にすれば、`math` モジュールのインポートが不要。
* `enumerate(nums)` を使う方がpythonic.
* `while` 内の `if` は親の継続条件にできる。

### Follow up

>Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

#### Divide and conquer

`log(n)` ということは分割統治法かな。
2つに割って、それぞれの配列での答えと、中央をまたぐ場合の答えとで、minを取る。
中央をまたぐ場合の実装が面倒。
まずは `target` を超えるまで右を延ばしていくが、超えたときと、右端に突き当たったときの2パターンがある。
また、左を延ばしたときに、右を縮められるかのチェックが必要。
さらに、これらの処理の中で都度minの更新をする。

https://github.com/naoto-iwase/leetcode/pull/50/changes#r2483829525

>半分に割って分割統治することを繰り返すという方法があります。中央をまたぐ場合とまたがない場合に分類します。

見当は合ってたっぽい。

#### Prefix sum & binary search

`log(n)` で連想するのは、あと二分探索。
累積和と合わせて解けそう。

`target = 7`, `nums = [2,3,1,2,4,3]` の場合を考える。
このとき `prefix_sum = [2, 5, 6, 8, 12, 15]`.
`for i, n in enumerate(nums)` に対して、条件を満たす配列の長さを求め、最小を更新する。
いま、`nums[2] = 1` から始まる、条件を満たす配列を探したい。
`target` までは残り 7 - 1 = 6.
`prefix_sum[i]` は `nums[i]` までの和で、`prefix_sum[j] - prefix_sum[i]` で
`i+1` から `j` までの和を求められる。
残り6を、`prefix_sum[i] - prefix_sum[2]` から二分探索すればよい。これは引数keyで指定できる。

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/48

sliding windowによる実装。

>不変条件として常にtargetより小さいという条件でスライディングウィンドウ

次のループに引き継ぐときの条件を考える。

>ループ開始時にendをインクリメントした方が自然だと考えfor文にした

これは同意。`while` 文は、カウンタの更新を忘れるリスクや、
更新が後に来るので冒頭で「これはちゃんと終わるのか？」という心配がある。

#### https://github.com/naoto-iwase/leetcode/pull/50

累積和＆二分探索（実装2）。
`prefix_sum` から、`target + prefix_sum[start]` を探してもいい。
つまり `(target + prefix_sum[start]) - prefix_sum[start] = target` ということになる。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.p6d6fndbrthh

https://github.com/SuperHotDogCat/coding-interview/pull/31#discussion_r1647128733

>right は含まないようにするのもありですか。なんか、right += 1 と prefix_sum += nums[right] が分裂しているのがちょっと気になります。

ポインタと、それが指すデータの処理（ここでは`total`への加算）を近くに置く。

