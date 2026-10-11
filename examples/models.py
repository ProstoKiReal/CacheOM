from cache_om import CacheModel, IntegerField, StringField


class SessionCacheModel(CacheModel):
    key_prefix = "session"
    ttl = 60 * 60

    user_id = IntegerField()
    role = StringField()
