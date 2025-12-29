## step 1

メールアドレスの規約を適用して、実際にユニークなメールアドレスの数を返す。  
仕様を読んでそのとおりにメールアドレスを正規化すれば良さそう。  
与えられるメールアドレスの数を `N`, メールアドレスの文字数を `M` とすると、メールアドレスひとつあたりの時間計算量は `O(M)`. したがって全体では `O(NM)`.

- `@` を境にしたlocalとdomainの分割：`O(M)`
- local nameにて
  - `+` 以下を捨てる：`O(M)`
  - `.` を無視する：`O(M)`

空間計算量は、重複排除のためにlocalとdomainを持っておくため `O(NM)`.

## step 2

パース部分を切り出してみた。また、メールアドレスを走査するのを一度だけにした実装もやってみた。  
こちらの方が理論上速そうだが、`str.split()` や `.replace()` の方がネイティブ実行なので実際速いみたい。  
可読性も拡張性も低そうなので、Pythonで書くならもとの実装を選ぶと思う。

### 他の人のコード

https://github.com/Yuto729/LeetCode_arai60/blob/d966a8218194705abe6ad9000bdc07c3a3eb7d76/unique-email-addresses/main.md

`@`を2つ以上含むことがありえる。RFC5322（とChatGPT）によると、local にクオートした `@` を含むのは正当みたい。  
https://datatracker.ietf.org/doc/html/rfc5322#section-3.4.1

https://github.com/Yoshiki-Iwasa/Arai60/pull/13#discussion_r1649832719

>とりあえず、ユースケースの想定ですね。これ、そもそもなんでこんなものを作りたいんだと思いますか。  
>たとえば、これ、マーケティングのメールを送りたいのか、ある集団のやりとりを整理したいのか。  
>つまり、たとえば、誤った入力が一つ入ったときに、全体として、そこそこ動いて欲しいのか、異常だといって止まって欲しいのか。それは何をしたいのかとの兼ね合いになるでしょう。

顧客リストにマーケティングのメールを送りたいとすると、そこそこ動いてほしい＝invalidなメールアドレスは飛ばしてログに落とす。  
全体が正しくないと止まってほしいケースは何があるかな…。一括ユーザー登録のような、トランザクション性のある処理なら、後でアドホックな対応をすることが比較的コストが高いので、まとめて弾きたいかも。

`str.split()` に `maxsplit` なる引数がある。maxsplit+1に分けてくれる。  
https://docs.python.org/ja/3.13/library/stdtypes.html#str.split

`str.partition()` というメソッドもある。こっちのほうがシンプルで速いらしい。  
https://github.com/yas-2023/leetcode_arai60/pull/14/files#r2423473701

少なくとも実装が違うことは確認（単なるラッパーではない）。

- partition: https://github.com/python/cpython/blob/3.13/Objects/unicodeobject.c#L12791-L12792
- split: https://github.com/python/cpython/blob/3.13/Objects/unicodeobject.c#L10118-L10119

正規表現を使うパターンもある。可読性が低いので選ばなさそう。  
https://github.com/yas-2023/leetcode_arai60/blob/afbb4fdcb9e76405e116e2232042ce5b9ffb0034/929/step3.py

### コメント集

https://github.com/hayashi-ay/leetcode/blob/2e5af6c462dc876cda45f78e071084bcc414d53f/929.%20Unique%20Email%20Addresses.md

>https://github.com/python/cpython/blob/bb3e0c240bc60fe08d332ff5955d54197f79751c/Objects/unicodeobject.c#L11768 文字列の追加 += が最適化される条件はここにあります。 背景として、Python の文字列がイミュータブルであることは常識なので、このコードを見たら誰もが不安にかられるので、その不安感を共有できていますか、という質問です。

`canonicalize` なるほど。ChatGPT曰く、`normalize` よりも「仕様の決まっている正解にまとめる」ニュアンスが強いらしい。

https://github.com/plushn/SWE-Arai60/pull/14#discussion_r2051724883

>これは一般論として正しいです。気にするとなお良い点が2つあります。
>メールアドレスの長さは最大どれくらいなのか。そのうえで2乗であることは問題なのか。
>メールアドレスはどこから来るのか。ユーザーからの入力であると思われるので、悪意のある入力が入ってくる可能性があるのではないか。

strがimmutableなので`+=`するたびに生成されることに続けて。

https://github.com/syoshida20/leetcode/pull/20#discussion_r2079714768

>あと、ユースケース考えて書いてますか。ユーザーがゴミを1つ突っ込んできたら例外投げて動かないコードでいいんですか。結論がいいならそれはひとつなんですが、私は考慮された形跡がないことを怖がってます。

## step 3

マーケティングメール一斉送信の想定で書いてみる。バリデーションもできる限り実装してみる。

