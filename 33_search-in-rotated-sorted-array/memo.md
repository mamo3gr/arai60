## step 1

昇順ソートされた上で、いくらかleft rotateされた配列 `nums` の中から `target` の位置を返す。
見つからない場合は -1 を返す。`nums` は最長5000である。

`O(log n)` での探索を求められているので、二分探索を使うのだろうことは想像がつく。
シンプルには、rotateを補正した上で単純な二分探索をする、というのが思いつく。
前問の[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)を使うと`O(log n)`で回転の回数は調べられるが、
メモリ上のデータでrotateを補正するとなると `O(N)` かかる。

補正するのではなく、崖になっている左側と右側をそれぞれ二分探索すればいいか。

## step 2

二分探索を2回から1回に減らせないか？と思って試行錯誤してみたがダメだったので、
他の人のコードやLeetCodeのソリューションを見ながら書く。
ポイントはmidよりも左側あるいは右側のどちらかはソートされていること、ソートされている側にtargetが入りうるかを考えること、らしい。

leftとrightの不変条件がこんがらがる。等号・不等号ガチャを始めたりして良くない。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.427rioitx1u6

https://discord.com/channels/1084280443945353267/1233295449985650688/1239594872697262121

`bisect_left` にkeyを渡して探索させる解法。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def cmp(a, b):
            return (a > b) - (a < b)
        def priority(x):
            return (nums[0] <= x) * -2 + cmp(x, target)
        i = bisect_left(nums, priority(target), key=priority)
        if i >= len(nums):
            return -1
        if nums[i] != target:
            return -1
        return i
```

priorityの意味が全くわからない。

>bisect_left key を使うと綺麗に行くかしら。
> 
>target が、nums[0] 以上のとき、
>nums[0] 以上 target 未満
>target
>target より大
>nums[0] 未満
>の順に並ぶはずです。
>nums[0] 未満のときは、
>nums[0] 以上
>target 未満
>target
>target 以上 nums[0] 未満
>ですね。
> 
>まとめると、
>nums[0] 以上 -2
>target 未満 -1
>targetと同じ 0
>target より大 +1
>nums[0] 未満 +2
>の和を計算して、-2 か +2 かを探せばよいのかしら。

言われたら分かったけど、自分では思いつけないなー。

https://github.com/Yoshiki-Iwasa/Arai60/pull/36#discussion_r1712955053

スカラーのpriorityではなく、`(崖の左右どちらにいるか, 数字)` のtupleでの実装。

```python
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def priority(x: int) -> int:
            return (x <= nums[-1], x)

        index = bisect.bisect_left(nums, priority(target), key=priority)
        if index < len(nums) and nums[index] == target:
            return index
        return -1
```

priorityの第1キーは、崖の左側か右側かを表す。False=0はTrue=1よりも優先度的に上。
第2キーは数字そのもの。
単なる要素の数字としては昇順ソートされていないが、何らかの変換で昇順にできれば、二分探索が適用できるわけだ。なるほど。

### 他の人のコード

#### https://github.com/skypenguins/coding-practice/pull/29

Step3. `left=0`, `right=len(nums)-1` と、`left <= i <= right` にtargetが存在するつもりで探索し、
leftとrightを追い越したら-1を返す (not found). ループの中で`nums[mid]`がtargetに当たれば返す。

#### https://github.com/garunitule/coding_practice/pull/43

Step2の後半。

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # targetはleft自身と以降左にあり、rightより右にはないと思っている
        left = 0
        right = len(nums) - 1

        while left <= right:  # leftがrightを追い越すまで
            mid = (left + right) // 2
            # max(nums) の左側を山、右側を谷と呼ぶ。
            # midが山側にあり、かつtargetが谷側にあるなら、mid以前は捨てていい
            if nums[-1] < nums[mid] and target <= nums[-1]:
                left = mid + 1
                continue
            # midが谷側にあり、かつtargetが山側にあるなら、mid以降は捨てていい
            if nums[mid] <= nums[-1] and nums[-1] < target:
                right = mid - 1
                continue 1

            # midもtargetも山側にある、またはmidもtargetも谷側にあるなら、
            # 通常の二分探索になる
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # targetは、leftとそれより右にあり、かつrightよりも右にはない。
        # つまりtargetが存在するとしたらleftの位置
        if left < len(nums) and nums[left] == target:
            return left
        return -1
```

#### https://github.com/naoto-iwase/leetcode/pull/26

bisectで崖を見つけた上で、左側（山側）あるいは右側（谷側）のどちらかをさらにbisectで探す (step1)。
`target <= nums[-1]` の条件で、targetが山側と谷側のどちらにいるのかわかる。

## step 3

- (a) 条件分岐付きの二分探索
- (b) 最小値（もとの左端）を見つける→二分探索する
- (c) keyをいじって二分探索する

の3パターンをやってみた。
(a) はまだ等号・不等号やインデックスの扱いが怪しい。また戻ってきてやる。

