## step 1

- ノードを辿っていって、都度訪問済みかどうかを判定したら良さそう。
- 訪問済みのノードはsetに格納する。ノードを一意に特定するにはidが使えそう。
  - setへのメンバーシップ判定 (in) はハッシュテーブルを引くだけなので（ほぼ）定数時間
  - listへのinは線形探索なので要素数に比例する
    - https://github.com/python/cpython/blob/v3.13.11/Objects/listobject.c#L664-L676
- constraintsからノードの最大数は10^4. すべてのノードのidを格納しても10^4 * 8byte = 80KB

