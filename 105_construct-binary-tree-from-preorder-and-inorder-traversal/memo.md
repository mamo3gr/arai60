## step 1

ある木のpreorder, inorderのtraversalが与えられたとき、その木を作って返す問題。  
preorderの先頭は根である。同じ値をinorderで探す。inorderでは、この値よりも左が左の部分木で、右も同様である。あとは再帰して部分木を繋げていけばよい。リストが空ならNoneにする。

計算量を見積もる。ノード数を `N` とすると、必要な処理は

* preorderの先頭を取り出す：`O(1)`
* inorderの中から同じ値 (root_val) を探す：`O(N)`
* root_valから左をコピーして再帰する：`O(N)`
  * コピーにかかる時間のつもり
* root_valから右をコピーして再帰する：`O(N)`
  * 左と合わせて、`N-2`個のコピーになる
* TreeNodeを作る：`O(1)`

という感じ。1回の再帰でノードがひとつできるので、`N`回繰り返すことになる。つまり `O(N^2)`.
制約より、preorderの要素数は最大3000個なので、Pythonの処理能力を10^7 steps/sec とすると、3000^2 / 10^7 = 0.9秒。ステップ数を1としたので（簡単のために、`N^2`が支配的だろうから）、1秒くらいのオーダーだと見積もれる。

次はメモリ。3000^2 = 9MB. これくらいのオーダーで必要になる。これまでの問題に比べるとかなり大きい。

ここまで書いてきて、見えている改善点を書いておく。コードの整理がてらstep 2で取り組む。

* 再帰で次に渡す配列は、コピーではなくインデックスにすると、メモリ使用量が減らせる
* inorderから値を探す `O(N)` はもっと減らせそう

rightで揃えるため、`preorder_right = preorder[-len(inorder_right):]` でpreorderの右部分木を取ろうとしたがハマった。長さ0のとき、`inorder[-0:]` となりリスト全体が返ってしまう。

## step 2

とりあえず再帰のまま、スライスのコピーをやめてインデックスで管理する。  
区間を表すdataclassを作ると便利そう。名前として `span`, `interval`, `range` あたりが思いつき、`range` は予約ごと被る、`interval` は長いので `span` を採用。  
インデックスの操作に苦戦する。いつまで経っても苦手だ、これ。

もともとの関数ではlistを受け取っているので、代わりにインデックスを受け取るヘルパー関数を用意する。名前はひねらなくていいだろう。

あと、`inorder` から任意の数字の位置を見つけるため、数字->インデックスのハッシュマップを用意しておく。

ここまで書けると、iterativeへの変更も比較的かんたんに見えてくる。  
preorder, inorderそれぞれの区間と、値を入れる先のノードをスタックに積んでやれば良い。

### 他の人のコード

#### https://github.com/docto-rin/leetcode/pull/34

>- 実装  
>  - preorderを順に走査してnodeを生成していく。  
>  - 左に進んでいき、stackに入れていく。  
>    - stack内は、左は処理済み（子を紐付け済み）だが右は未処理なノード  
>  - stack[-1].valがinorder[inorder_cursor]と異なれば左に進み、等しければ一歩ずつ翻っていく。  
>  - 一歩ずつ翻っていくとき、stack[-1].valがinorder[inorder]と異なるノードに出会ったら、その左の子の右の子としてnodeを紐づける。  

別解。

#### https://github.com/nanae772/leetcode-arai60/pull/29

再帰 (step2). 自分の場合はpreorderとinorderとで区間を持っていたが、inorderの区間とpreorderの開始だけを引き継いでいる。たしかにpreorderで欲しいのは先頭のインデックスだけだ。

冒頭で`preorder`, `inorder`の長さが等しいかチェックしている。これも丁寧。

#### https://github.com/garunitule/coding_practice/pull/29

改めてスライスを引き継ぐコードを見ているけど、可読性でいったらこっちのほうが圧倒的に良いよなあ。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.1rv0z8fm6lc3

https://github.com/goto-untrapped/Arai60/pull/53#discussion_r1777944717

>これ、典型的な小さい例から考える、みたいなことをしているんですが、たとえば、1, 2, 3 の3要素からなる木を全部列挙して、5通りあるはずですが、それぞれがどういう値になるか、くらいから考えてみたらどうでしょうか。

>あー、あと、遅いコードでもいいから動くものを書いてみませんか。一回書けると速くしやすいです。

解法の見つけ方。今回はうまくできた方だと思う。

https://github.com/fuga-98/arai60/pull/29#discussion_r2020242408

さらに別解。inorderの順に生成していく。

https://github.com/Yoshiki-Iwasa/Arai60/pull/33#discussion_r1688357607

`array.array` を使うと、スライスをコピーしなくても書ける。  
https://docs.python.org/3.13/library/array.html  
numpyにしちゃうのも有力とのこと。

### preorderベースの構築

https://github.com/docto-rin/leetcode/pull/34 で見かけた別解を、自分なりに咀嚼して書いてみる。  

* `preorder[0]` は root になる。rootをスタックに積む。
* inorderの配列を見ていくインデックスを用意する。左端=0で初期化する。
* `preorder[1]` から順に、ノードを作り、どこに付けるかを判断する。大まかに言えば、スタック末尾のノードの左か、右である
* スタック末尾の値と、inorderの値が等しいなら、それは木の左端に到達したということである。このときの操作は後述する
* 左端に到達していないなら、スタック末尾のノードの左に新しいノードを付ける
* 左端に到達しているなら、新しいノードはスタック内のノードのうち、 **いずれかの** ノードの右に付く
  * 接続先は、inorderインデックスのインクリメントと合わせてpopしていったとき、値が等しい最後のノードである（条件を満たさなくなった、直前のノード）
* どちらの場合でも、付けたノードをスタックに乗せる

いきなりrootを置くよりも、番兵 (dummy) を置いたほうがしっくりくる。  
特に、新しいノードを右の子に持つ親を探す際に、whileを抜けた直前ループでのpop結果を使う、という分かりにくい書き方になってしまう。

```python
while potential_parents and potential_parents[-1].val == inorder[inorder_i]:
    parent_of_right_child = potential_parents.pop()
    inorder_i += 1
```

番兵を置いておくと、popして条件を満たしたら抜ける（いまpopしたノードを採用）、ということが分かりやすい。ちなみに `None` はintと比較するとFalseになるので、番兵ノードのvalをNoneにしておくとif文の条件を必ず満たせる。

```python
while potential_parents:
    parent_of_right_child = potential_parents.pop()
    inorder_i += 1

    if potential_parents[-1].val != inorder[inorder_i]:
        break
```

### inorderベースの構築

発想が難しい。  
https://github.com/nittoco/leetcode/pull/37, https://github.com/fuga-98/arai60/pull/29#discussion_r2020242408 あたりを参考にやる。

Geminiに壁打ちしてもらいながら書いたが、あんまり腹落ちしていない。特に、スタックに積まれたノードに対し、右に数珠つなぎにして動くあたり。

## step 3

本当は不要なんだけど、preorderでの終点も持っておく（区間のdataclassを使う）のが、すっきりするししっくりくる。
