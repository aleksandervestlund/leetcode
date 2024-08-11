from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        value = self.lru.get(key, -1)
        if value != -1:
            self.lru.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.move_to_end(key)
        elif len(self.lru) == self.capacity:
            self.lru.popitem(last=False)
        self.lru[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)