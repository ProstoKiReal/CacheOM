import time
from typing import Any
from uuid import UUID, uuid4

import pytest

from cache_om import CacheModel, IntegerField, StringField


@pytest.mark.skip(reason="Not implemented")
def test_create_and_get_round_trip(cache_client):
    class CachedSession(CacheModel):
        key_prefix = "test:session"
        ttl = 60

        user_id = IntegerField()
        role = StringField()

    sessions = CachedSession.objects.using(cache_client)
    created = sessions.create(user_id=123, role="admin")
    loaded = sessions.get(uid=created.uid)

    assert isinstance(created.uid, UUID)
    assert loaded is not None
    assert loaded.uid == created.uid
    assert loaded.user_id == 123
    assert loaded.role == "admin"


@pytest.mark.skip(reason="Not implemented")
def test_get_returns_none_for_cache_miss(cache_client):
    class CachedSession(CacheModel):
        key_prefix = "test:session-miss"
        user_id = IntegerField()
        role = StringField()

    assert CachedSession.objects.using(cache_client).get(uid=uuid4()) is None


@pytest.mark.skip(reason="Not implemented")
def test_save_updates_existing_cached_model(cache_client):
    class CachedSession(CacheModel):
        key_prefix = "test:session-update"

        user_id = IntegerField()
        role = StringField()

    sessions = CachedSession.objects.using(cache_client)
    session = sessions.create(user_id=123, role="admin")
    session.role = "user"
    session.save()

    loaded = sessions.get(uid=session.uid)

    assert loaded is not None
    assert loaded.role == "user"


@pytest.mark.skip(reason="Not implemented")
def test_delete_removes_cached_model(cache_client: Any) -> None:
    class CachedSession(CacheModel):
        key_prefix = "test:session-delete"

        user_id = IntegerField()
        role = StringField()

    sessions = CachedSession.objects.using(cache_client)
    session = sessions.create(user_id=123, role="admin")
    uid = session.uid

    session.delete()

    assert sessions.get(uid=uid) is None


@pytest.mark.skip(reason="Not implemented")
def test_model_ttl_expires_cached_model(cache_client: Any) -> None:
    class ShortLivedSession(CacheModel):
        key_prefix = "test:session-ttl"
        ttl = 1

        user_id = IntegerField()
        role = StringField()

    sessions = ShortLivedSession.objects.using(cache_client)
    session = sessions.create(user_id=123, role="admin")

    assert sessions.get(uid=session.uid) is not None

    time.sleep(1.2)

    assert sessions.get(uid=session.uid) is None
