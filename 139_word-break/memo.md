## step 1

文字列 `s` と辞書 `wordDict: list[str]` が与えられ、辞書内の単語のつなぎ合わせで `s` が作れるか、をbooleanで返す。  
`s` は最長300, `len(wordDict)` は最長1000, `1 <= len(wordDict[i]) <= 20`.

`s` の先頭を `for word in wordDict` と一致したら切り取って、残りをスタックに積んでいけば良さそう。
時間計算量はどう見積もろう。`s` の長さを `L`, 辞書の語彙数を `W` とする。
簡単のため、辞書に含まれる単語は1文字にする。すると、
`s` から1文字を取り除くのに `O(W)` 必要で、それを `L` 回繰り返す。
こう書くと `O(WL)` に見えるが正しいか？実際には探索木を行ったりきたりするのだが、これを反映されてない気がする。
正しいとして、Pythonの処理能力を10^7 steps/sec とすると 300 x 1000 / 10^7 = 30ミリ秒くらいのオーダーを予想する。  
メモリについては、スタックに `O(L)` が必要そう（1文字切り取る、2文字切り取る、…、を全部積んだと仮定）。300 * 4 bytes/char = 1.2 KBくらいを予想する。

以下のケースでTime Limit Exceededしてしまった。

```python
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
```

`s` を切り取った結果をsubstringと呼ぶとすると、同じsubstringを何度もスタックに積んでいる。
この重複を排除するために、setを使う。
このsetのおかげで、さらに `O(L)` の空間計算量が必要になる。ただしオーダーは変わらない。

