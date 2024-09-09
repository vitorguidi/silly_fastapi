from storage.db.database import Database
from storage.db.database_provider import database_provider
from typing import Annotated
import uvicorn
import os

from fastapi import Depends, FastAPI

app = FastAPI()

async def get_config() -> str:
    with open(os.getenv('CONFIG_PATH')) as config_json:
        return config_json.read()

async def get_db(config: Annotated[dict[str, any], Depends(get_config)]) -> Database:
    return database_provider(config)

@app.get("/items/{item_id}")
def get_item(item_id: str, db: Annotated[Database, Depends(get_db)]):
    #Todo: handle 404
    return db.get_item(item_id)

@app.put("/items/{item_id}/{item_value}")
def get_item(item_id: str, item_value: int, db: Annotated[Database, Depends(get_db)]):
    db.put_item(item_id, item_value)
    return 'ok'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)