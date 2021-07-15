import redis
import time
import pytest
from datetime import datetime

# 레디스 연결
rd = redis.Redis(host='localhost', port=6379, db=0)

@pytest.fixture()
def test_key():
    tt = round(time.time() * 1000)

    key = f'test_key_{tt}'
    yield key
    rd.delete(key)


def test_increment_count(test_key):
    rd.incr(test_key)

    ii = int(rd.get(test_key))
    assert ii == 1

    rd.incr(test_key)
    ii = int(rd.get(test_key))

    assert ii == 2


def test_set(test_key):
    rd.sadd(test_key, 'hello')
    rd.sadd(test_key, 'hello')
    rd.sadd(test_key, 'world')

    members = rd.smembers(test_key)
    ss = ['world', 'hello']
    for idx, mem in enumerate(members):
        assert mem.decode() == ss[idx]
