## step 1

与えられた文字列のうち、重複のない最初の文字の位置を返す。  
重複しているかどうかは、ハッシュマップを使えばよい。  
位置はkey=文字、value=位置のdictで覚えておくか。  
先頭から一文字ずつ処理していけば良い。この走査の時間計算量は `O(N)`（ただし文字数を `N`）で、ハッシュマップとdictの操作は `O(1)`.  
ユニークな文字の種類数を `M` とすると、空間計算量は `O(M)` になる。すべての文字がユニークとすると 2M 個の要素を記憶することになる（ハッシュマップと位置）。  
Python 3.7から、辞書の要素が挿入順に取り出せるのでありがたい（インデックスでのソートが不要）。

## step 2

最初に思いついたアルゴリズムでは、ハッシュマップとdictの2つを管理するのでやや煩雑だった。例えば、重複があったらdictからも要素を削除する必要があるが、削除済みである場合も考慮しなくてはいけない。  
「重複している場合は位置=-1」とすれば、dictだけで済む。  
ただしデメリットとして、最後にインデックスを調べるときには、-1でない値が出てくるまでdictをループして取り出す必要がある。重複する文字が多いときは比較的時間がかかる。文字列は最長で 10^5.

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/blob/c60d31f74ff18947b112e044a1938501eadf6a24/first-unique-character-in-a-string/main.md

key=char, value=indexのlistを作って、最後に len(list)==1 の要素だけを取り出すパターン。これがnaiveな実装だったか。

>文字をキューに入れて2回以上出現する文字を取り除いていくやり方もある https://github.com/colorbox/leetcode/pull/29/changes/BASE..48f2749be9c4ec78c6f24c887880e34c7206f678#r1861430039

dictがOrderedDictでないならこんな解き方になるのかも。

https://github.com/komdoroid/arai60/pull/5

OrderedDictの実装はdoubly-linked list.  
https://github.com/Fuminiton/LeetCode/pull/30#discussion_r2040649727

>これ、OrderedDict の中身は Doubly-Linked List なので、まあ、練習としては、Doubly-Linked List 自体を書いて欲しいところではありますね。

https://github.com/yas-2023/leetcode_arai60/pull/15

- `Counter` を使う選択肢もある。これも文字の登場順にdictが作られるはず。
  - コードはシンプルになるが、都合、文字列を2回走査することになる
- `find` を使う選択肢は思いつかなかった。理論上の計算量は `O(N^2)` になるが、`find` 自体の実行が速い。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.hdbcrwo3urck

## TODO

- [ ] Doubly-Linked Listの実装

