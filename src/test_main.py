from main import app, get_config
from fastapi.testclient import TestClient
import json

client = TestClient(app)

async def test_config() -> str:
    return json.dumps({
        'db': {
            'db_type': 'in_memory',
        }
    })

app.dependency_overrides[get_config] = test_config

def test_can_set_and_get_value():
    response=client.get("/items/2")
    print(response)
    assert response.content == b'null'
    client.put("/items/2/3")
    print(response.content)
    response=client.get("/items/2")
    assert response.content == b'3'