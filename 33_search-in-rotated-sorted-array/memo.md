## step 1

昇順ソートされた上で、いくらかleft rotateされた配列 `nums` の中から `target` の位置を返す。
見つからない場合は -1 を返す。`nums` は最長5000である。

`O(log n)` での探索を求められているので、二分探索を使うのだろうことは想像がつく。
シンプルには、rotateを補正した上で単純な二分探索をする、というのが思いつく。
前問の[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)を使うと`O(log n)`で回転の回数は調べられるが、
メモリ上のデータでrotateを補正するとなると `O(N)` かかる。

補正するのではなく、崖になっている左側と右側をそれぞれ二分探索すればいいか。

