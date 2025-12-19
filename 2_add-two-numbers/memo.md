## step 1

- 桁の繰り上がりを保存しながら、2つの数を足した結果をノードに追加していけばよさそう。

## step 2

- 同じような処理を関数にまとめて、見通しをよくする。

### 他の人のコード

https://github.com/komdoroid/arai60/blob/31deeca5c9a0feb74b7dd0fd7a9be92d386f5715/2.AddTwoNumbers/step2.py

再帰で書くパターン。現在の桁の合計は `% 10` する方がスマートか。

https://github.com/resumit30minutes/leetcode-arai60-practice/blob/7c31041bc3f35ffa52f6637ef74afaf9d644f4a0/leetcode/add_two_numbers/step4.py

`l1`, `l2` だけでなく `carry` の有無もwhile文の条件に入れると、ループを抜けた後のcarryを付け足す必要がないのね。なるほどー。

https://github.com/Yuto729/LeetCode_arai60/blob/77e1bd492d015d806913a1fa06e1b8ab89009b88/2.AddTwoNumbers/step4.py#L17

ノードから値を取り出して、同時に次のノードへの参照を返す関数を定義する。コードとしてはすっきりするが、違う操作をまとめてしまっており個人的にはやりすぎ。

### コメント集

- `None` のままではなくて `ListNode(0)` にする方法。なるほど

https://discord.com/channels/1084280443945353267/1366423240624439378/1372611463872516096

- `zip_longest` と `yield` を使った解法。Pythonの機能を使って、些末な作業（ノードの遷移とか、もうノードがない場合の処理とか）を押し出しているという点で素晴らしい

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def generate_digits(l):
            while l:
                yield l.val
                l = l.next
        dummy = ListNode()
        node = dummy
        carry = 0
        for num1, num2 in zip_longest(generate_digits(l1), generate_digits(l2), fillvalue=0):
            total = num1 + num2 + carry
            node.next = ListNode(total % 10)
            node = node.next
            carry = total // 10
        if carry:
            node.next = ListNode(carry)
        return dummy.next
```

