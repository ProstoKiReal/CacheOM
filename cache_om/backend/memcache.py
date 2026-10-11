from pymemcache.client.hash import HashClient

from cache_om.backend.base import CacheBackend


class MemcacheBackend(CacheBackend):
    def __init__(self, client: HashClient):
        self.client = client
