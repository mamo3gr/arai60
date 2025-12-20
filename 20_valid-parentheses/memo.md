## step 1

- カッコの対応が取れているかを調べる問題
  - 開きカッコはスタックに積みつつ、
  - 閉じカッコに出会ったらスタックから取り出して対応を調べれば良い

## step 2

- カッコの対応が取れているか調べる関数をくくりだす
- 開きカッコの集合は tuple で定義しておく
  - 候補はlist, tuple, set
  - 要素数が多いならsetの方が有利。ハッシュテーブルで引くので
  - 今回は要素が3つなのでlistかtupleの方がオーバーヘッドが少ないと思われる
  - 要素は固定なのでtuple
- popしつつ、例外をキャッチしてスタックの空を検出する

### 他の人のコード

https://github.com/komdoroid/arai60/blob/493492a824e13fde5b11cf811431213e44b30773/20.ValidParentheses/step2-1.py

```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = deque()
        open_to_close = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
            
            elif ch in open_to_close.values():
                if not open_brackets or open_to_close[open_brackets.pop()] != ch:
                    return False
        
        if len(open_brackets) != 0:
            return False
        return True
```

- カッコの対応を辞書で持っておく手。なるほどー
  - `open_to_close` だが、反対の引き方もありそう
  - ループのたびに `.values()` を呼び出すのはちょっと非効率に思える

https://github.com/resumit30minutes/leetcode-arai60-practice/blob/1fed0e211f2a256992f2eeb619d956ade9adabe0/leetcode/valid_parentheses/step3.py

```python

class Solution:
    def isValid(self, s: str) -> bool:
        open_to_closed_brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        expected_closed_brackets = []
        for c in s:
            if c in open_to_closed_brackets:
                expected_closed_brackets.append(open_to_closed_brackets[c])
                continue

            if expected_closed_brackets == []:
                return False

            if expected_closed_brackets[-1] != c:
                return False
            expected_closed_brackets.pop()

        return expected_closed_brackets == []
```

- `pop` ってlistも変更しつつ値も返すので、よく考えると忙しいメソッドだ。
- ループを抜けた後に、スタックが空かどうかを戻り値にする書き方もあるんだ。

https://github.com/Yuto729/LeetCode_arai60/blob/d663a98bf0bca81c47461319daea111ced973979/valid-parentheses/main.md#step3

```python
class Solution:
        def isValid(self, s: str) -> bool:
            open_branckets = []
            open_to_close = {
                '(': ')',
                '{': '}',
                '[': ']'
            }

            for char in s:
                if char in open_to_close:
                    open_branckets.append(char)
                    continue

                if not open_branckets or open_to_close[open_branckets.pop()] != char:
                    return False

            return len(open_branckets) == 0
```

- スタックが空かどうか、popしつつdictを引いて現在見ている文字と比較する、というのをまとめてやっていて、認知負荷が大きい。ここは分けて書いたほうがわかりやすそう。

### コメント集

- https://github.com/bumbuboon/Leetcode/pull/7#discussion_r1817837783
  - スタックの底に、番兵として、いずれにもマッチしない文字列を置いておく。なるほど
- https://discord.com/channels/1084280443945353267/1225849404037009609/1231648833914802267
  - 将来的にカッコ以外の文字列も入る可能性を考えてみよう、とのこと
- https://github.com/yus-yus/leetcode/pull/6#discussion_r1944970090
  - 「副作用のある式を条件に書きたくない」なるほど
- `'({[': str` に対して `in` しても判定できる。
