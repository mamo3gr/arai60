import pytest
from priority_queue import PriorityQueue


def test_basic_functionality():
    """基本的な追加と取り出しの順序を確認"""
    pq = PriorityQueue()
    items = [10, 5, 15, 2]
    for item in items:
        pq.push(item)

    assert pq.pop() == 2
    assert pq.pop() == 5
    assert pq.pop() == 10
    assert pq.pop() == 15
    assert pq.is_empty() is True


def test_duplicate_values():
    """重複する値が含まれる場合の挙動を確認"""
    pq = PriorityQueue()
    for item in [5, 1, 5, 3]:
        pq.push(item)

    assert pq.pop() == 1
    assert pq.pop() == 3
    assert pq.pop() == 5
    assert pq.pop() == 5


def test_peek_and_len():
    """peekが値を削除せずに取得できること、lenが正しく更新されることを確認"""
    pq = PriorityQueue()
    pq.push(20)
    pq.push(10)

    assert len(pq) == 2
    assert pq.peek() == 10
    assert len(pq) == 2  # peek後はサイズが変わらないこと
    assert pq.pop() == 10
    assert len(pq) == 1


def test_empty_pop():
    """空のキューからpopしようとした時に例外が発生することを確認"""
    pq = PriorityQueue()
    with pytest.raises(ValueError):
        pq.pop()


def test_random_large_input():
    """大量のランダムな数値で正しくソートされるか確認"""
    import random

    data = [random.randint(0, 1000) for _ in range(100)]
    pq = PriorityQueue()
    for x in data:
        pq.push(x)

    results = []
    while not pq.is_empty():
        results.append(pq.pop())

    assert results == sorted(data)
