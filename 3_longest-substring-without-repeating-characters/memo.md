## step 1

文字列 `s` が与えられたとき、重複する文字の無い、最長の部分文字列について、その長さを返す。
制約として `s` の長さは `0 <= s.length <= 5 * 10^4` である。

素朴な解法としては、`for each i in range(len(s))` に対して、`i` 文字目から始まる、
重複のない部分文字列の長さを求める。最後にmaxを取ればよい。
これだと時間計算量は `O(N^2)` かかる。ただし、`N = len(s)` である。
Pythonの処理能力を 10^7 steps/sec とすると、(5 * 10^4)^2 / 10^7 = 250秒のオーダーになりTLEする。

`i` から始まる部分文字列と、`i+1` から始まる部分文字列の調査は、重複している文字がほとんどになるはず。
部分文字列を一文字ずつ読んでいって重複が無いかチェックする。これにはsetを使う。
重複があったら、そこで部分文字列の長さを求めて、最大値を更新する。
いま調べている部分文字列の先頭インデックス `start_i` を覚えておき、これをインクリメントすれば良い。
あわせて `s[start_i]` をsetから削除する。

これで時間計算量が `O(N)` になる。5 * 10^4 / 10^7 = 5ミリ秒くらいのオーダーで終わる。
空間計算量も `O(N)`. `s` に重複がない場合、setにすべての文字を含む。
5 * 10^4 * 4 bytes/char = 200 KB くらいのオーダーを予想する。

書いてみたが、テストケース `nfpdmpi` で躓いてしまった。
6文字目の `p` を読むとき、ここまで読んできた文字 `nfpdm` と重複があるので調査を打ち切る。
次に調査する部分文字列の開始インデックス `start_i` はインクリメントするだけでは足りない。
というのも、`fpdm` にはまだ `p` が含まれているから。
`p` を含まない先頭まで移動させる必要がある。移動にあわせて、そこまでの文字もsetから取り除く。

これでテストをパスした。

## step 2

GeminiとChatGPTにレビューしてもらいつつ、コードを整理する。

* forループを抜けたあとの最大値更新処理がトリッキーなので、ループ内に押し込む
  * 長さが確定していなくても、現在の長さを使って更新できる
* そもそもsetではなく、dictで文字ごとのインデックスを管理すれば、いちいちsetから文字を取り除かなくて良い

どちらのパターンでも書いてみた。

### 他の人のコード

#### https://github.com/garunitule/coding_practice/pull/47

start, endでのsliding window.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        max_length = 0
        char_to_next_index = {}
        while end < len(s):
            if s[end] in char_to_next_index:
                start = max(start, char_to_next_index[s[end]])
            max_length = max(max_length, end - start + 1)
            char_to_next_index[s[end]] = end + 1
            end += 1

        return max_length
```

辞書として、key=文字、value=次に文字が現れたときstartを更新するインデックスを管理している。
このvalueが分かりにくい。単に「文字が最後に現れたインデックス」の保持が良いと思う。

また、個人的な感覚として、whileはいつ終わるのか不安になる
（本文を読まないと、条件に含まれる変数がどう更新されるのか分からないから）。
ここもforの方が安心する。

#### https://github.com/h1rosaka/arai60/pull/49

DPっぽい考え方 (step 1).

>「このマスが終着点だった時に、最高の長さは」を各マスに記録していく
>既出の文字が発生した場合、そこより前の文字列は使用不可として考える

実質的にはsliding windowになっている。
startの更新はmaxを使ったほうが分かりやすそう。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        char_to_last_index = {s[0]: 0}
        safe_begin_point = 0
        for i in range(1, len(s)):
            char = s[i]
            if char in char_to_last_index:
                safe_begin_point = max(
                    safe_begin_point,
                    char_to_last_index[char] + 1
                )
            dp[i] = i - safe_begin_point + 1
            char_to_last_index[char] = i
        return max(dp)
```

#### https://github.com/naoto-iwase/leetcode/pull/49

setやdictではなく `str.find()` を使う (step 1).
時間計算量としては `O(N^2)` のようだがTLEしない。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = 0
        max_length = 0
        for last in range(1, len(s)):
            found = s.find(s[last], first, last)
            if found == -1:
                continue
            # substring is from first to last - 1
            max_length = max(max_length, last - first)
            first = found + 1
        return max(max_length, len(s) - first)
```

`char_to_index.get(c, -1)` として条件分岐をなくす (step2).
コードとしてはすっきりするけど、読み手からしたらシミュレートの手間が増えそう。

### コメント集

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.shly89hponxm

https://github.com/olsen-blue/Arai60/pull/49#discussion_r2005295464

>seen_char_to_index.get(s[right], -1)
>と使えば、条件分岐を回避できますね。

さっきのPRと同上。

