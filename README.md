How to run:
CONFIG_PATH=config.json poetry run python3 src/main.py
if running redis, start the daemon and config.json should be
{
    "db": {
        "db_type": "redis",
        "host": "localhost",
        "port": 63789,
    }
}

if running in memory kvs, do:
{
    "db": {
        "db_type": "in_memory",
    }
}

How to test:
poetry run python3 -m pytest