## step 1

- テストの点数がストリームで入力されるので、そのたびにk番目に高い点数を返す
- k番目までの点数をソート済みで覚えておき、新しい点数が入ってきたら然るべき場所に入れたらいい。その後でk+1番目を切り落とし、k番目の点数を返す
- 現状の知識の範囲でやるなら、listをbisectで二分探索して適切な挿入位置を調べる、かな
- Geminiに聞いたら3つあるらしい
  - listのbisect: 最大値を返すのにO(1), 挿入にO(n)
    - linked listになっているなら挿入にはO(n)かからなさそう。あとで実装を調べてみたい
  - 優先度付きキュー：O(1), O(log n)
  - 二分探索木：O(log n), O(log n)
- 優先度付きキューには `heapq` という実装がある：https://docs.python.org/3/library/heapq.html
- min-heapでk番目までの点数を覚えておく。heapの先頭が返す値である

## step 2

- ヒープの長さを整える処理がコンストラクタと `add` で共通しているので、メソッドに切り出してまとめる。

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/blob/ab29bfb2d55ee44d41c63e41f02f6bbf93280869/kth-largest-element-in-a-stream/main.md#step3

- 保持する数列に説明的な変数名を付けるのは良い：`self.top_k_values`. 
  これだと順序が分からないので、`_ascending` とか付けると尚良いかも。
- 優先度付きキューの実装はやっておきたい。

https://github.com/kazizi55/coding-challenges/blob/42e8b4e450bdcea12db9570fc853f162b47b809f/arai60/703-kth-largest-element-in-a-stream/step4.py

- コンストラクタでの処理を `add` で共通化しちゃうパターン、なるほど

https://github.com/yas-2023/leetcode_arai60/blob/85cc0c72e88035d0b7026dec87e20cd2ac484feb/703/step3_heapq.py

- 自分の感覚に近い。

### コメント

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.t2w1qof72ib2

ざっと眺めた。

