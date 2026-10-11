import os

import pytest
from pymemcache.client.hash import HashClient

from cache_om import CacheClient, MemcacheBackend


@pytest.fixture
def memcache_client():
    client = HashClient(["localhost", 11211])
    try:
        yield client
    finally:
        client.close()


@pytest.fixture
def memcache_backend(memcache_client):
    return MemcacheBackend(client=memcache_client)


@pytest.fixture
def cache_client(memcache_backend):
    return CacheClient(backend=memcache_backend)
