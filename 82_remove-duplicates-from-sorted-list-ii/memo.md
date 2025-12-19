## step 1

- 昔解いた記憶があるが完全に想起できてない。もう一度解説動画を見つつ書き直す。
- 次と、次の次のノードを見る、というのが前問に比べて複雑。whileの条件分岐が末端・エッジケースで正しく機能するのかパッと分からない。

## step 2

### 他の人のコード

https://github.com/komdoroid/arai60/blob/9773f5844b4ff3ca2b817195b1ad9b6d0a70deab/82.RemoveDuplicatesFromSortedListII/step2-3.py

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last_fixed_node = dummy

        while head:
            if head.next is None or head.val != head.next.val:
                head = head.nextn
                last_fixed_node = last_fixed_node.next
                continue
            duplicate_val = head.val
            while head and head.val == duplicate_val:
                head = head.next
            last_fixed_node.next = head
        
        return dummy.next
```

- headを書き換えちゃうのは怖い（もとの参照をdummy.nextに保存しているとはいえ）
- 処理中の `head` は、`last_fixed_node` の次を見たいのだと思うが、それが名に現れているとよい。そもそも二重管理気味にも見える
- スキップしたい値を `duplicate_val` と置くのは良い

https://github.com/aki235/Arai60/blob/5c5e6ed61dfd7c0b19eb766a3119793aba21fd41/82_Remove_Duplicates_from_Sorted_List_II.md

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed_node = dummy
        node = head

        while node and node.next:
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                last_fixed_node.next = node.next
            else:
                last_fixed_node = last_fixed_node.next
            node = node.next
        
        return dummy.next
```

- `last_fixed_node` という命名はよい
- while文の条件は、`last_fixed_node` を起点にした書き方がわかりやすそう。頭の中で `last_fixed_node` と `node` の中身を管理する必要があるので

https://github.com/Yuto729/LeetCode_arai60/blob/7bd37b04c8e7ca272ea05b6eb32a89d038dfe9fd/remove-duplicates-from-sorted-list-ii/main.py

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head

        while current is not None:
            if current.next is None or current.val != current.next.val:
                previous = current
                current = current.next
                continue

            value_to_delete = current.val

            while current is not None and current.val == value_to_delete:
                current = current.next

            previous.next = current

        return dummy.next
```

- `previous` よりは `fixed` のようなニュアンスが欲しい
- `if current.next is None or current.val != current.next.val` の条件は、同じ処理をしても最終的に問題はないが、意味は違う：「比べる次のノードが無い」のと「次と、次の次のノードで値が違う」。分けたほうがわかりよい

https://github.com/resumit30minutes/leetcode-arai60-practice/blob/5b998735c530633a08b5509ed639cb082bcd553c/leetcode/remove_duplicates_from_sorted_list2/step3.py

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        node = head

        while node is not None and node.next is not None:
            if node.val != node.next.val:
                tail = node
                node = node.next
                continue

            value_to_remove = node.val
            while node is not None and node.val == value_to_remove:
                node = node.next
            tail.next = node

        return dummy.next
```

- 細かいけど、もう変更しないつもりの値はコンストラクタで書いてしまうのが良い：`dummy.next`
- 着目する値を変数に置くのは良い：`value_to_remove`
- `tail` は `fixed` のニュアンスを入れたい

https://github.com/MasukagamiHinata/Arai60/blob/12d15eda0b111b259c2d225565377dd791daef0a/82.-Remove-Dupliccates-from-Sorted-List-II.py


```python
class Solution:
    def _skip_duplicates(self, current: Optional[ListNode]) -> Optional[ListNode]:
        while current.next is not None and current.val == current.next.val:
            current = current.next
        return current

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        IMPOSSIBLE_VAL = -100
        dummy = ListNode(IMPOSSIBLE_VAL, head)
        current = head
        previous = dummy
        while current is not None:
            if current.next is not None and current.val == current.next.val:
                last_duplicate = self._skip_duplicates(current)
                previous.next = last_duplicate.next
                current = last_duplicate.next
            else:
                previous = current
                current = current.next
        return dummy.next
```

- 関数に切り出しているのが良い：`skip_duplicates`. 返ってくるノードがどっちなのか（重複する最後のノードなのか、その次なのか）がわかると尚よい

## 書き直す

これが比較的しっくりくる。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed = dummy
        while last_fixed.next and last_fixed.next.next:
            if last_fixed.next.val != last_fixed.next.next.val:
                last_fixed = last_fixed.next
                continue
            
            connect_to = last_fixed.next
            while connect_to.next and connect_to.val == connect_to.next:
                connect_to = connect_to.next
            last_fixed.next = connect_to

        return dummy.next
```

「重複があるノードを始点として、その重複の終わりを探す」部分を関数として括りだすパターン。これも悪くない

```
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed = dummy

        def find_duplicates_end(head) -> Optional[ListNode]:
            node = head
            while node.next and node.val == node.next.val:
                node = node.next
            return node

        while last_fixed.next and last_fixed.next.next:
            if last_fixed.next.val != last_fixed.next.next.val:
                last_fixed = last_fixed.next
                continue

            last_fixed.next = find_duplicates_end(last_fixed.next).next

        return dummy.next
```


## コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.xzxd7jwvkwc5 から。ループで何を引き継ぐか。なるほどなー。

重複削除中のフラグを導入して書くパターンもあるのか。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed = dummy

        number_to_skip: int | None = None
        checking = last_fixed.next
        while last_fixed:
            if number_to_skip is None:
                if checking is None:
                    break

                if checking.next and checking.val == checking.next.val:
                    number_to_skip = checking.val
                    continue
                else:
                    last_fixed.next = checking
                    last_fixed = last_fixed.next
                    checking = checking.next
                continue

            if checking is None:
                last_fixed.next = None
                break

            if checking.val == number_to_skip:
                checking = checking.next
            else:
                number_to_skip = None

        return dummy.next
```

自分なりに書いてみるとこんな感じ。今見ているノードを変数で表す方が分かりやすそう（二重管理にもなるのでケースバイケースだが）。状態 `number_to_skip` が増えたせいでロジックが複雑になる。1ループにつき1ノードを調べる制約がないなら、このパターンは選ばないなあ。重複を見つけた時点で、その重複の末尾まで進んでしまいたい。

