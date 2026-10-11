from uuid import UUID

from cache_om.backend import MemcacheBackend
from cache_om.client import CacheClient


def create_app():
    cache_client = CacheClient(host="localhost", port=11211)
    cache = MemcacheBackend(client=cache_client)
    # app = FastAPI()
    # Somethig with app
    # return app
