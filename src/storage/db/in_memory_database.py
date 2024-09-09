from storage.db.database import Database


class InMemoryDatabase(Database):
    def __init__(self):
        self.db = dict()

    def get_item(self, key: str) -> any:
        return self.db.get(key, None)
    
    def put_item(self, key: str, val: any):
        self.db[key] = val

    def delete_item(self, key: str):
        del self.db[key]
