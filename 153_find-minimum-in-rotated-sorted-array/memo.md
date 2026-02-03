## step 1

昇順ソート済みの配列 `nums` （長さ `n`）が、1からnまでのいずれかの回数だけrotateされている。
rotateとは、末尾の要素を先頭に回し、残りを右に移動する操作である。
このとき、`nums` の中で最小値を求める。`1 <= n <= 5000` である。

テストケースの `[3,4,5,1,2]` を見てみると、これは3回rotateされている。
そして、`nums[3]` が求める最小値である。
つまり、`nums[num_rotate]` を求めればよい。
また、昇順ソート済みであるから `nums[i] < nums[i+1]` が成り立つはずだが、
`nums[num_rotate-1]` と `nums[num_rotate]` の間では成り立たない。
この境界を見つけるといいんじゃないかな。

`O(N)` のアルゴリズムなら、隣り合う要素を順番に見ていけば良さそう。
ただし、問題文から `O(logN)` を求められている。
となると、二分探索するのが筋に思う。

`first = 0` から `last = len(nums) - 1` の間のどこかに、前述の境界があるつもりで探索を始める。
ただし、はじめから昇順ソート済み、つまり `len(nums)` 回rotateされている、
あるいはlastの右側に境界がある、というケースがあるので、これは先に弾いておく。
`mid` を取れば、そこから左側か右側のどちらかは単調増加しているはずだから、その側を探索範囲から外す。
ループを抜けるときには、`first` と `last` が隣り合っていて、この間が「崖」になっているはずだから、
`nums[last]` を返せば良い。

これで時間計算量は `O(logN)` になるはず。
処理時間として、log5000 / 10^7 [steps/sec] = 1.2マイクロ秒くらいのオーダーを予想する。
つかうメモリは、`first` と `last` の2つのインデックスで、28 bytes * 2 = 56 bytes.

## step 2

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/42

step1は自分と同じ実装。

>nums[left] > nums[right]が成り立つ一番狭い区間を探せばよさそう

この書き方、明快だ。

step2,3では、`nums[mid]` と比較する要素を `nums[0]` に固定するバージョン。
どうしてこれで動くんだろう。コメントを付けながら考えてみる。

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 回転なしの場合はearly return
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            # nums[0] <= nums[left] つまり、
            # 0 <= i <= left では nums[0] から単調増加している
            if nums[0] <= nums[mid]:
                left = mid
            else:
                # nums[right] < nums[0] だから、
                # right <= i <= len(nums)-1 では単調増加している
                right = mid

        # ループを抜けるとき left + 1 >= right だから、
        # leftとrightはこの順で隣り合っている。
        # 0からleftと、rightから末尾までがそれぞれ単調増加しているから、
        # 崖があるとしたらこの間にある。
        return nums[right]
```

`nums[0]` から `nums[left]` まで登っていき、ここと `nums[right]` の間に崖があって、
`nums[right]` から末尾までまた登っていく。leftとrightを狭めていくと、それらが隣り合ったとき、
もとめる崖になっている。

さらに、`nums[-1]` と比較するバージョン。  
https://github.com/garunitule/coding_practice/pull/42/changes#r2633207600  
ソート済みである場合のearly returnが不要になるらしい。こちらも読んでみる。

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        """invariant:
        - for all i <= left, nums[i] > nums[-1]
        - for all i >= right, nums[i] <= nums[-1]
        """
        left = -1
        right = len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        return nums[right]
```

`nums[-1]` を基準として、`left` までは大きい側、
`right` から末尾までは小さい側。

>これはなぜか、説明できますでしょうか。

動作的には…、
回転なしの場合、rightが毎ループで左に移動してきて、
最後にはleft=-1,right=0となり、`nums[0]` が返る。
探索によって更新された結果、`right` は `nums[-1]` よりも小さい一番左のインデックスを指すようになる。
これは回転があってもなくても変わらない。

`nums[-1]` という比較対象の位置というより、探索の初期値とその動かし方から、
回転なしの場合を取り込めているかどうか、というのが分かれ目に思える。
前述の `nums[0]` と比較するコードでは、
`left, right = 0, len(nums) - 1` で初期化していて `nums[right]` を返す。
だから、探す境界が-1と0の間に（あるいは `len(nums)` と0 の間に）ある場合が取り込めていない。
これを取り込むようにすることは可能である（例えば以下のようにする）。
ただし、`nums[-1]` と比較するバージョンの方が、回転なしの場合をより自然に取り込めているように感じる。

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid]:
                left = mid
            else:
                right = mid

        # right = len(nums) であれば循環して0を指すようにする
        return nums[right % len(nums)]
```

Geminiと壁打ちしてみたら「`nums[right] <= nums[-1]` のグループに、いつも答えが含まれているから」らしい。

#### https://github.com/naoto-iwase/leetcode/pull/25

`bisect_left` を使った実装（実装3）。  
https://docs.python.org/3.13/library/bisect.html#bisect.bisect_left
`nums` は、 `nums[0]` よりも大きい左側と、`nums[-1]` より小さい右側に分かれる。
引数 `key` でラムダ式が渡せるので、`nums[-1]` との大小がTrue/Falseで表現でき、
その境界を二分探索できる。自分でも書いてみよう。

さらに、ラムダ式の代わりに `Sequence` を継承してTrue/Falseを返すビュワークラスを実装するパターン（実装4）。`__getitem__` と `__len__` を実装すればいいらしい。

step3 では、`left` と `right` に不変条件をコメントしている。
これも変数名で短く表現するのが難しいので良い工夫。

#### https://github.com/seal-azarashi/leetcode/pull/39/changes/BASE..683d2b2992abcb3569a92a2708648c60d952b83b#r1846593786

```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] <= nums[right]) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return nums[left];
    }
}
```

* Question
  * Answer
* 2で割る処理がありますがこれは切り捨てでも切り上げでも構わないのでしょうか。
  * 構わない。midがleftとrightの間に入れば良い。
* `nums[middle] <= nums[right]` とありますが、これは < でもいいですか。
  * いい。本問ではnumsに含まれる要素はユニークなので差はない。
* `nums[right]` は、`nums[nums.length - 1]` でもいいですか。
  * いい。末尾から左に向かって単調減少しているはずで、`right`はその範囲を、最も左に向かって動かしている。
    したがって `nums[middle]` と比べる相手としてどちらでもよい。
* right の初期値は nums.length でもいいですか。
  * そのままだとout of indexになってしまう。`nums[middle]` を `nums[nums.length - 1]` と比べる場合なら動く。

https://github.com/seal-azarashi/leetcode/pull/39#discussion_r1851404872

>補足すると、目的を設定し、目的に必要な手段を決め、手段を粒度の大きい部分から小さい部分に向かって検討していく、という思考ができていないように感じました。また、粒度の大きい部分を、木構造のように再帰的に小さい部分に分割して思考するということもできていないように感じました。この辺りを意識しながら思考の仕方を改善されることをおすすめいたします。

思考のフレームワークが未熟なので、こういう言語化をしてもらえると助かる。

#### https://github.com/yas-2023/leetcode_arai60/pull/22

回転部分＝大小が逆になる崖を探しに行く。
`nums[middle] > nums[right]` なら `left = middle + 1` という更新をしており、
`right` を見て `left` を更新するのが何で？となった。
（`middle` と `right` の間に求める崖があるので、`left` をそこまで詰める、という発想）

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.tzbo5j6mbqc2

https://discord.com/channels/1084280443945353267/1230079550923341835/1233971372946882600

>いましていることをメタ的にいうと、選択肢、つまり、考察の幅自体を広げたいと思っています。
>
>nums[0] <= nums[i] な領域と nums[0] > nums[i] な領域の境界を探せ
>nums[-1] < nums[i]  な領域と nums[-1] >= nums[i] な領域の境界を探せ
>
>ともいえますね。

選択肢の幅を広げる。境界を探すので、比較対象は両端のどちらかにもできる。

https://discord.com/channels/1084280443945353267/1230079550923341835/1235694567085576275

`bisect_right` でも書ける。

https://github.com/takuya576/leetcode/pull/2#discussion_r2055670305

>ループはある種の仕事の引き継ぎのようなもので、どういうものだと思って引き継いでいるのか、それが変数名などで初めて読んだ人にもある程度通じるのか、を意識して書くといいでしょう。

## step 3

末尾と比べるのがすっきり書けるが、そうだと分かっているからそれを選んでいる気もする（過学習）。
3ヶ月後くらいに再度解いたら、先頭と比べるパターンを書きそう。

