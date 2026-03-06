""" "ChatGPTに生成させた、自作LRUCache向けのテストコード"""

import pytest

from my_lru_cache import MyLRUCache


def test_basic_put_get():
    cache = MyLRUCache(1)

    cache.put("a", 1)

    assert cache.get("a") == 1


def test_key_error():
    cache = MyLRUCache(1)

    with pytest.raises(KeyError):
        cache.get("missing")


def test_update_value():
    cache = MyLRUCache(1)

    cache.put("a", 1)
    cache.put("a", 10)

    assert cache.get("a") == 10


def test_eviction():
    cache = MyLRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)

    with pytest.raises(KeyError):
        cache.get("a")

    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_get_updates_lru():
    cache = MyLRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)

    cache.get("a")  # a becomes most recent

    cache.put("c", 3)

    with pytest.raises(KeyError):
        cache.get("b")

    assert cache.get("a") == 1
    assert cache.get("c") == 3


def test_capacity_one():
    cache = MyLRUCache(1)

    cache.put("a", 1)
    cache.put("b", 2)

    with pytest.raises(KeyError):
        cache.get("a")

    assert cache.get("b") == 2


def test_repeated_get():
    cache = MyLRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)

    assert cache.get("a") == 1
    assert cache.get("a") == 1
    assert cache.get("a") == 1


def test_order_complex():
    cache = MyLRUCache(3)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)

    cache.get("a")
    cache.get("b")

    cache.put("d", 4)

    with pytest.raises(KeyError):
        cache.get("c")

    assert cache.get("a") == 1
    assert cache.get("b") == 2
    assert cache.get("d") == 4


def test_put_existing_key_updates_lru():
    cache = MyLRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)

    cache.put("a", 10)  # should make "a" most recently used

    cache.put("c", 3)

    # b should be evicted
    with pytest.raises(KeyError):
        cache.get("b")

    assert cache.get("a") == 10
    assert cache.get("c") == 3
