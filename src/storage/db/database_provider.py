from storage.db.redis_database import RedisDatabase
from storage.db.in_memory_database import InMemoryDatabase
from storage.db.database import Database
import json
import functools

@functools.lru_cache
def database_provider(config: str) -> Database:
    config = json.loads(config)
    assert 'db' in config
    config = config['db']
    db_type = config.get('db_type', None)
    assert db_type is not None
    match db_type:
        case 'redis':
            assert 'host' in config
            assert 'port' in config
            return RedisDatabase(config.get('host'), config.get('port'))
        case 'in_memory':
            return InMemoryDatabase()
        case _:
            raise f'Unsupported database config type: {config}'
