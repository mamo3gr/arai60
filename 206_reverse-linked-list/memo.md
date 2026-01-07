## step 1

- ノードを順に辿っていって、前のノードに繋ぎ変えれば良い。
  - 繋ぎ変える先を取っておく必要がある
  - 進める先も記憶しておく必要がある
- 結構こんがらがるなー

## step 2

### 他の人のコード

https://github.com/resumit30minutes/leetcode-arai60-practice/blob/bb0d5c1df5dd90b2e89bf431c2447944ef75000b/leetcode/reverse_linked_list/step3.py

```python
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        reversed_head = head
        node = head.next
        reversed_head.next = None
        while node is not None:
            tmp = node.next
            node.next = reversed_head
            reversed_head = node
            
            node = tmp
            
        return reversed_head
```

- 考え方は同じ
- `tmp` はより具体的な方が良い
- `reversed_head` は、`head` じゃないこともあるのでミスリーティング。`_next` とかがより適切か

https://github.com/Yuto729/LeetCode_arai60/blob/cb904fb5b4989d83f955baa85ee47fca2e4baba5/reverse-linked-list/main.md#step2-follw-up-他の人のコードを読む

再帰でも書けるのか。

>再帰、各ノードに人を立たせて見たらいいと思うんですよ。  
>考え方としては、5番目の人が6番目の人に、何を渡して、何を返してもらうか、だと思います。  
>
>頭から5番目までひっくり返した物を渡して、全部がひっくり返ったものを返してもらう。  
>何も渡さずに、6番目以降をひっくり返したものを返してもらう。  
>くらいじゃないでしょうか。  
>その時に、頭と尻尾を渡さないと、作業するのに困る場合がありますね。

## step 3

もとのリストのノードを順に見ていって、ノードごとにリンクをひっくり返す。  
見ているノード `working` をwhileループの継続条件にすると、ループを抜けた後で返すheadが `working` のひとつ前になるのが微妙。ということで、ややこなれないが、while Trueにしてループ内で条件判定する。

