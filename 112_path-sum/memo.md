## step 1

二分木と `targetSum` が与えられて、和がそれに等しい root-to-leaf path を持っているかどうかを判定する問題。ノード数は最大5000で、値は負の数もありえる。

rootからそれまでの和を覚えながら辿っていき、leafに着いたときに `targetSum` と等しいか判定すれば良さそう。再帰でもキューでも書けるが、再帰がぴったり当てはまりそうに思うので、まずは再帰で書いてみる。早く返せるかどうかは、条件に当てはまるleaf nodeの深さに依存しているので、一般には再帰とキューのどちらが優れているかは言えなさそう。【追記】再帰は親まで返るオーバーヘッドがかかる。とはいえ大差ないと思う

時間計算量は、ノード数を `N` とすると最良で `O(log N)`（最初のleafで条件を満たす）、最悪で `O(N)`. 処理としては (1) `node.val` を覚えている和に足す、(2) leafか判定する、(3) 子ノードに対して再帰する、くらいなので3ステップと仮定すると、3 * 5000 / 10^6 [steps/sec] = 15ミリ秒くらいのオーダーを予想する。  
使うメモリは、子ノードを調べるときに、スタックが高々 `log N` 必要。log(5000) = 16.6くらいで、Pythonの一般的な再帰呼び出し上限は1000なので、かなり余裕がある。

ノード数は0があり得るので、`root is None` の判定が必要。このロジックにまかせて、子ノードが `None` かどうかを気にせず再帰しちゃう（関数本体の短さを優先）。

## step 2

キュー（というかスタック）で書いてみる。再帰の場合は、与えられた関数をそのまま再帰した（ヘルパーを書かなかった）ので、`targetSum` から `node.val` を引いた新しいターゲットを引き継いでいたが、スタックを用いた実装では「あるノードまでの和 (`total`)」を覚えておいて、それを `targetSum` と比べることにした。この方が自然に感じるので。  
ノードが `None` の処理は、`root is None` の場合も兼ねてループの中に押し込めるかどうかを考えた。入れる場合は、子ノードがnot Noneか気にせずスタックに積めるが余計にループが回る。入れない場合はその反対。leaf nodeの判定とそれで分岐した処理のネストが浅くなることもあり、後者＝入れないを選択した。

### 他の人のコード

#### https://github.com/plushn/SWE-Arai60/pull/25

`append_if_exists` なるinner functionを使うパターン。  
https://github.com/plushn/SWE-Arai60/pull/25/files#r2649175416

減算・加算の議論。

`is_leaf` なら `targetSum` に等しいかどうかでTrue/Falseを返しちゃえばよかったんだ。

#### https://github.com/naoto-iwase/leetcode/pull/29

>もし葉でtargetSumになるような経路を返却するとしたらどうでしょうか？  
>設問としてはTrue/Falseなのですが、単純にTrue/Falseを得るよりはpathを実際に知るほうが意味があるのかなと思ったので...自分が面接だったら質問しそうです。

この視点は無かった。なるほど。
https://github.com/naoto-iwase/leetcode/pull/29/files#r2455081026

>chromiumのコードにもfrontiersは出てきますね。

`frontiers`, 自分にはなじみが無かったけどメジャーなんだな。  
https://github.com/naoto-iwase/leetcode/pull/29/files#r2455081958

#### https://github.com/nanae772/leetcode-arai60/pull/25

>is_leafはTreeNodeのメソッドにしたい（LeetCodeの仕様として出来ない（無理やりsetattrなどすればできる？））、  
>ないしはSolutionから独立した関数としたほうがよいのではないかという意見があった。

TreeNodeのメソッドにしたいのは同意。

inner functionを再帰して、親の変数として「見つかった」フラグを使う。あるいは、Exceptionで帯域脱出する。step1では気が付かなかったが、再帰では根本まで処理を返す必要があるのに対し、スタックを使う実装では見つけ次第関数を終了できる。そこまで大きな差ではないと思うが…

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.ed3x3pkyeqkp

