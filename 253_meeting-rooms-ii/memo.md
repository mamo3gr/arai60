## step 1

会議の開始・終了を含むオブジェクト `Interval` の配列が与えられたとき、
会議がconflictしない最小の会議室数を返す。制約は次の通り。

* 0 <= `intervals.length` <= 500
* 0 <= `intervals[i].start` < `intervals[i].end` <= 1,000,000

前問での解法の応用が効きそう。
各 `Interval` に対し、開始時に会議室の `demand` を `+1`, 終了時に `-1` する。
あとは時間帯で積分して（累積和をとって）、途中の最大値を求めれば良い。

会議数を `N`, 時刻の最大値を `T = 1,000,000` として、実装の方針を検討する。

a. `[0] * T` のスケジュール配列を作って、`+1` と `-1` を書き込む。
   * `O(T)` の補助空間が必要。10^6 * 28 bytes/int = 28MBくらいのオーダー。
     最後に累積和を取るにも `O(T)` かかる。
b. 座標圧縮してから `+1`, `-1` を書き込む。
   * 時刻をソートするのに `O(N logN)` かかるが、補助空間も `O(N)` で済む。
c. `intervals` をソートして、`demand` を順に足していく。
   * ソートに `O(N logN)`, 補助空間は `O(N)`（ソートした配列を格納する）。
d．`intervals` をheapに入れて、popしながら足していく。
   * すべて取り出すのに `O(N logN)`, 補助空間は `O(N)`.

d. でheapを使うよりは c. の方が複雑さは減りそう。
a. はやりたいことに対して補助空間を使いすぎるように思うので b. を優先したい。
b. と c. を比べて c. の方がシンプルに思う（座標を圧縮するよりも、直接並び替える方がシンプル）。
ということで c. をまずは書いてみる。

## step 2

ChatGPTにレビューしてもらいつつ、コードを整理する。

* `Event` クラスは少し過剰。tupleで十分
  * 実装としては過剰かもしれないが説明的なのでヨシ
* `__lt__` は保守性が低い。`demand` が second key なのは分かりにくい
  * これはそうだなあ。コメントで補うか。
* `Event` の名前が少し曖昧
  * これ以上装飾しても大差ないように思う
* `min_rooms` 更新は `max` の方が読みやすい
  * まあどちらでも

さらに、heapとtwo-pointersの解法もあるらしい。これらにも取り組んでみる。

まずはtwo-pointers. startとendを分けてまとめ、それぞれソートする。これらを `starts`, `ends` とする。
`starts` と `ends` の先頭で、早い方を取り出す。
`starts` から取り出したら `rooms += 1`, `ends` から取り出したら `rooms -= 1`.
マージソートみたいだ。

次にheap.
`intervals` をソートする。
`end` をheapに入れていく。for interval in intervalsで、heapの先頭と `interval.start` を比べる。
つまり、いま見ている会議の開始より、前に終了している会議があるなら、heappopする。
最後にheapの長さが答えになる。
ちょっとパズルっぽい。
会議室が空く時間を早い順に並べてheapで管理していて、いま会議が来たら、最も早く空く部屋に間に合うかどうか、
を見ているということか。間に合うならその部屋を解放し (heappop), 新しい終了時刻を push する。

### 他の人のコード

#### https://github.com/Satorien/LeetCode/pull/55

heapではなくて `bisect.insort()` で管理するパターン (step3).
なるほど確かにこれでもできる。

#### https://github.com/tokuhirat/LeetCode/pull/56

座標圧縮、このようにシンプルに書けた。

```python
def coordinate_compression(coordinate: list[int]) -> dict[int, int]:
    coordinate = sorted(set(coordinate))
    return {value: i for i, value in enumerate(coordinate)}
```

#### https://github.com/shintaro1993/arai60/pull/60

heapアプローチ (step3).
heapの命名は `using_end_times` としている。より具体的でいいかも。

#### https://github.com/naoto-iwase/leetcode/pull/57

step1での実装（実装1, 2）が面白い。
まず終わるのが早い順にソート。アクティブな会議の終了時刻を `room_to_reserve: list[int]` で管理する。
for interval in intervalsに対し、開始時刻を `room_to_reserve` から二分探索 (`bisect_right`) する。
つまり、`room_to_reserve = [10, 20, 30]` に対し、`start = 25` とすると、
`20` に終わる部屋 (`room_to_reserve[1]`) を再利用できる。`bisect_right(start) - 1` で
この部屋のインデックスを求められる。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0

#### https://github.com/nittoco/leetcode/pull/45#discussion_r1996402752

>たとえば、ここの会社では、会議が始まるときに受付に鍵を借りに来て、終わるときに受付の郵便箱に返します。
>あなたは受付です。会議が始まるたびに、郵便箱の中の鍵を回収して、手持ちの鍵を渡します。
>会議室の予約の表が与えられるので、最低いくつ鍵が必要か答えてください。

#### https://github.com/olsen-blue/Arai60/pull/57#discussion_r2027474114

>解法の取りうる範囲の数字を全部挙げはじめたら結構驚くと思うんですよね。
>浮動小数点だったらこのままでは駄目ですよね。

これは同じ感覚だったので安心した。
