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
