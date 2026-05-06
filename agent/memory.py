# agent/memory.py

class Memory:
    def __init__(self):
        self.data = {}

    def store(self, key: str, value: str):
        self.data[key] = value

    def retrieve(self, key: str):
        return self.data.get(key)

    def has(self, key: str) -> bool:
        return key in self.data

    def all_data(self):
        return self.data