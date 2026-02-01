## step 1

整列済みでユニークな整数の配列 `nums` があり、与えられた値 (`target`) について配列中のインデックスを返す。
もし見つからない場合は、入るべきインデックスを返す。
つまり二分探索、Pythonでいう `bisect.bisect_left` を書け、という問題に見える。制約は次の通り。

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`

配列の中間の値（添字を `mid` とする）と `target` とを比べて、配列の左半分か、あるいは右半分を見つけに行く。再帰でもループでも書けそうだが、再帰のほうが素直に書けそう。配列長は最大で 10^4 で、スタックの深さは logN になるので、log10^4 = 13回くらいで済む。スタックオーバーフローのリスクは低そう。

処理時間を見積もる。探索回数は前述の通り `O(logN)` なので、Pythonの処理能力を 10^7 steps/sec とすると、
log10^4 / 10^7 = 1.3マイクロ秒くらいのオーダーを予想する。  
メモリについては、同様に `O(logN)` のスタックを積むことになる。
ChatGPTによると再帰あたりのフレームは1KBくらいらしいので、13KBくらいのオーダーを予想する。

何とか書けた。
分かりやすさの観点から閉区間で考えたが、再帰のときに端をデクリメントする必要がある（例えば`start, mid-1`. そうでないと、どちらか半分の探索が無限ループする）。
さらに、デクリメントする場合、`last` が `start` よりも小さくなる場合がある。

## step 2

ループでも書いてみた。やはりwhile文の条件と、左端・右端の処理が怪しい。

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/41

ループ。`left`, `right` としている以外は一緒っぽい。

https://nuc.hatenadiary.org/entry/2025/11/29/#二分探索を読めるか

>何を言っているかというと、二分探索で左だの右だの書いてあることがあるが、それが部隊内でどのような共通理解がなされているのかは必ず問題となるはずなのに、書いた本人もその理解がないまま書かれている場合がよくある。動くコードだとしても少し話をしてみるとなぜかここを理解せずに書いていることが分かるのだ。ここの了解があれば、あとは登る塔は必ず妥当か、必ず終了するのかと、終了時に欲しいものが出てくるのかくらいの問題でしかない。なぜか理解せずに覚えようとする人をよく見る。

これだった。PRのコメントを見ていると、コメント集から見たほうが良さそう。

### コメント集

#### https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.e13uiztrq2u9

https://github.com/Ryotaro25/leetcode_first60/pull/45#discussion_r1888181919

>「この関数の仕事を手作業でやっているとしましょう。シフト制で SearchInsertIndex の呼び出しが起きるごとに、人が交代します。
>あなたは、当番で SearchInsertIndex の呼び出しがおきたという連絡を受けて、仕事につきます。
>start, end, nums, target が与えられました。
>ここまで働いている人たちがきちんと仕事をしていたら、start, end, nums, target についてどのようなことがいえますか。」
>という質問に答えられますか。

https://github.com/seal-azarashi/leetcode/pull/38#discussion_r1836463140

>いや、私の抵抗感がどこから来ているかというと、left, right はそれぞれ何を満たしている値だと思ってループを回していて、それがループから出たときに何が満たされているのかの認識がふわふわしているように思っています。

ここのスレッドで言っていることが消化できれば良さそう。コードは https://github.com/seal-azarashi/leetcode/pull/38/changes/BASE..4ab989566c109e3379565dff7847ed058a92a05d#r1842919607 からコピーして、読みながらコメントを書く。`left` と `right` を更新する式から、それぞれを何だと思っているのか想像する。

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] == target) {
                return middle;
            }
            // leftよりも左はtargetよりも小さい。（left自身はまだ分からない）
            if (nums[middle] < target) {
                left = middle + 1;
            }
            // rightよりも右はtargetよりも大きい。（right自身はまだ分からない）
            if (target < nums[middle]) {
                right = middle - 1;
            }
        }
        // ループを抜けるとき、left == middle の状態からleftがインクリメント、あるいは
        // rightがデクリメントされるので、leftはrightのひとつ右を指す。
        // 不変条件から、leftよりも左はtargetより小さいはずで、
        // rightよりも右はtargetよりも大きいはず。
        // いま、leftはrightの右隣にある。したがって、rightとleftの間、
        // すなわちleftから右の要素を右に押しのけて、targetを挿入すればソート順が保たれる。
        return left;
    }
}
```

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] == target) {
                return middle;
            }
            // leftよりも左は、targetよりも小さい。
            if (nums[middle] < target) {
                left = middle + 1;
            } else {
                // target <= nums[middle] で、
                // nums[middle] == target ならreturnしているので、
                // rightとそれより右は、targetよりも大きい。
                right = middle;
            }
        }
        // ループを抜けるとき、left == rightになる。
        // 不変条件より、leftよりも左はtargetよりも小さく、
        // かつrightとそれより右はtargetよりも大きい。
        // いま、left == rightだから、これが指す要素を右に押しのけてtargetを挿入すれば、
        // ソート順が保たれる。
        return left;
    }
}
```

理解しながら書けるようになりつつあるが、スムーズに読めるだろうか。

https://discord.com/channels/1084280443945353267/1196498607977799853/1269532028819476562

>1. 二分探索を、 [false, false, false, ..., false, true, true, ture, ..., true] と並んだ配列があったとき、 false と true の境界の位置を求める問題、または一番左の true の位置を求める問題と捉えているか？
>2. 位置を求めるにあたり、答えが含まれる範囲を狭めていく問題と捉えているか？
>3. 範囲を考えるにあたり、閉区間・開区間・半開区間の違いを理解できているか？
>4. 用いた区間の種類に対し、適切な初期値を、理由を理解したうえで、設定できるか？
>5. 用いた区間の種類に対し、適切なループ不変条件を、理由を理解したうえで、設定できるか？
>6. 用いた区間の種類に対し、範囲を狭めるためのロジックを、理由を理解したうえで、適切に記述できるか？

#### https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.c15qprmvxkc2

https://github.com/philip82148/leetcode-swejp/pull/13#discussion_r2043982312

二分探索の読み方。

### 他の人のコード（つづき）

書くより読むのが大事とのことで、読みながら注釈をつけていく。
できる人は頭の中でできそうだが、自分は書きながらでないとできない。

#### https://github.com/yas-2023/leetcode_arai60/pull/21

##### step1.py

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1

        while (last_index - first_index) > 1:  # firstとlastが隣り合うまで
            current_index = (first_index + last_index) // 2
            if target >= nums[current_index]:
                # firstと左は、target以下である
                first_index = current_index
                continue
            # target < nums[current_index]
            # lastよりも右は、targetより大きい
            last_index = current_index

        # ループを抜けるとき、last - first == 1.
        # つまり、first,lastと隣り合っている。
        # first自身とそれより左は、target以下である。
        # かつ、lastよりも右はtargetより大きい。
        #
        # ..., first（target以下）, last, （targetよりも大きい）...
        #
        # targetの位置はまだ決まってない。

        if target == nums[first_index]:
            # first自身がtargetだったケースはここで拾えているが、
            return first_index
        # firstよりも左にtargetがあるケースが抜け落ちてる

        # lastよりも右はtargetより大きいが、
        # last自身がどうかは分からない。なので調べる
        if target <= nums[last_index]:
            # last自身がtarget以上なら、
            # target以下であるfirstと、last（target以上）の間にtargetを挿入すればよい
            return last_index
        # そうでないなら、last（targetより小さい）の右に挿入する
        return last_index + 1
```

「first自身がtargetである」ケースしか拾えていない。
「firstより左にtargetがある」ケースの分岐を足す必要がある。
すなわち、`target <= nums[first_index]` にすべき。
もとのコードではテストがパスしなかったが、この修正でパスするようになった。

余談だが、Geminiに聞いたら「元のままでも問題なく動く」と回答したので、
`nums=[1,3], target=0` のシミュレートをさせて誤回答であることを分からせた。
LLMは油断ならない。

##### step2_1_confusing.py

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [left, right] のどこかにtargetがあると考えてそう
        left = 0
        right = len(nums) - 1
        while left <= right:  # leftがrightを追い越すまで
            middle = (left + right) // 2
            if target <= nums[middle]:
                # rightよりも右は、target以上である
                right = middle - 1
            else:
                # nums[middle] < targetなので、
                # leftよりも左は、targetより小さい
                left = middle + 1

        # ループを抜けたとき、right, leftとなる。
        # 不変条件よりrightより右はtarget以上で、
        # leftより左はtargetより小さい。
        # したがってtargetはleftの位置に挿入するのが正しい。
        return left
```

##### step2_3.py

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 半開区間、つまりleft自身から、rightを含まない手前までにtargetがあると考える
        left_index = 0
        right_index = len(nums)

        while left_index < right_index:  # 抜けるとき、left == right
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index

            if middle_value < target:
                # leftよりも左はtargetより小さい
                left_index = middle_index + 1
            else:
                # target <= middle_valueで、
                # target == middle_valueであるときはearly returnするので、
                # rightと以降右はtargetより大きい
                right_index = middle_index

        # ループを抜けるとleft == right.
        # 不変条件からleftよりも左はtargetより小さく、
        # rightと以降右はtargetより大きい。
        # したがって、この位置にいる要素を右に押しのけて挿入すると、ソート順が保たれる。
        return left_index
```

コメント書きながらだと読めるな。
実際はそらでできることが求められるのだろうか。期待スピードも気になる。

##### step2_4.py

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 開区間で考えている。つまり、nums[left] < target < nums[right] を期待している。
        left_index = -1
        right_index = len(nums)

        while right_index - left_index > 1:  # 抜けるとき left, right と隣り合う
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index

            if middle_value < target:
                # leftと以降左はtargetより小さい
                left_index = middle_index
            else:
                # target <= nums[middle_index] だから、
                # rightと以降右はtarget以上
                right_index = middle_index

        # ループを抜けたとき、left, rightと隣り合う。不変条件から、
        # leftと以降左はtargetより小さく、
        # rightと以降右はtarget以上。
        # したがって、rightにある要素を押しのけて挿入すればソート順が保たれる。
        return right_index
```

開区間だと `right_index` を返すのが、これまでのパターンと違う。
いっけん奇妙に思えるが、不変条件を考えていくと正しいことが分かる。

#### https://github.com/naoto-iwase/leetcode/pull/24

`first_true` という考え方（実装5）。境界を見つけるってやつだ。同じく `last_true` も（実装6）。
