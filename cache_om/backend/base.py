from typing import Protocol
from abc import abstractmethod


class CacheBackend(Protocol):
    @abstractmethod
    def save(self, key: str, value: bytes, expire: int = 0):
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def update(self, key: str, value: bytes, expire: int = 0):
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str):
        raise NotImplementedError
