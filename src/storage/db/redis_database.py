import redis
from storage.db.database import Database


class RedisDatabase(Database):
    def __init__(self, host, port):
        self._redis = redis.Redis(host=host, port=port, decode_responses=True)

    def get_item(self, key: str) -> any:
        return self._redis.get(key)
    
    def put_item(self, key: str, val: any):
        self._redis.set(key, val)
