## step 1

動くコードが送信できればOK

- ノードを辿っていって、都度訪問済みかどうかを判定したら良さそう。
- 訪問済みのノードはsetに格納する。ノードを一意に特定するにはidが使えそう。
  - setへのメンバーシップ判定 (in) はハッシュテーブルを引くだけなので（ほぼ）定数時間
  - listへのinは線形探索なので要素数に比例する
    - https://github.com/python/cpython/blob/v3.13.11/Objects/listobject.c#L664-L676
- constraintsからノードの最大数は10^4. すべてのノードのidを格納しても10^4 * 8byte = 80KB

## step 2

コードを整える

- 引数の `head` を直接書き換えていく（mutateする）のはお行儀が悪いので、ノードを辿るためのポインタは別な変数にすべき
  - step1では `current` だったが、現在見ている **ノード** の意味で `node` の方がやや適切に思う
- nodeのidは2回引くよりも、一度引いて `node_id` に格納する
- ifの分岐はelseよりもearly returnにする。条件が真のときが特殊なケース（処理が終了する）で、偽のときとはやや非対称に思うので

他の人のコード、コメントも見てみる

- https://github.com/komdoroid/arai60/pull/8 を見ると、ノードのインスタンス `ListNode` をそのままsetに入れている。これでもいいのかー
  - setは要素の `__hash__` を使ってハッシュテーブルを作っている。このハッシュを引いた後に `__eq__` で同一判定をする
  - 一般的なクラスのインスタンスは、idそのもの、あるいはidベースのハッシュを返す `__hash__` が実装されている

```python
Python 3.14.2 (main, Dec  5 2025, 16:49:16) [Clang 17.0.0 (clang-1700.4.4.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> class A:
...     pass
...
>>> a = A()
>>> id(a)
4425857216
>>> b = A()
>>> id(b)
4426310480
>>> aa = a
>>> id(aa)
4425857216
>>> a.__hash__()
276616076
>>> b.__hash__()
276644405
>>> aa.__hash__()
276616076
```

- two pointersを使う方法も書いた。https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.2k4z0wt6ytf9 で言及されているように、setを使った方法が書ければOKらしい。

