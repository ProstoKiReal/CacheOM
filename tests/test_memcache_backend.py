import time
from uuid import uuid4

import pytest


@pytest.mark.skip(reason="Not implemented")
def test_save_and_get_bytes(memcache_backend):
    key = f"test:backend:{uuid4()}"
    value = b'{"role":"admin"}'

    memcache_backend.save(key, value)

    assert memcache_backend.get(key) == value


@pytest.mark.skip(reason="Not implemented")
def test_get_returns_none_for_missing_key(memcache_backend):
    assert memcache_backend.get(f"test:backend-missing:{uuid4()}") is None


@pytest.mark.skip(reason="Not implemented")
def test_update_replaces_existing_value(memcache_backend):
    key = f"test:backend:{uuid4()}"
    memcache_backend.save(key, b"before")

    memcache_backend.update(key, b"after")

    assert memcache_backend.get(key) == b"after"


@pytest.mark.skip(reason="Not implemented")
def test_delete_removes_value(memcache_backend):
    key = f"test:backend:{uuid4()}"
    memcache_backend.save(key, b"value")

    memcache_backend.delete(key)

    assert memcache_backend.get(key) is None


@pytest.mark.skip(reason="Not implemented")
def test_save_respects_expiration(memcache_backend):
    key = f"test:backend-ttl:{uuid4()}"
    memcache_backend.save(key, b"expires", expire=1)
    assert memcache_backend.get(key) == b"expires"

    time.sleep(1.2)

    assert memcache_backend.get(key) is None
