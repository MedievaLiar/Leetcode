# Beats 80% 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.max_capacity = capacity
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value = self.cache.pop(key)
        self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache.update({key : value})
        else:
            self.cache.update({key : value})
            if len(self.cache) > self.max_capacity:
                LRUKey = next(iter(self.cache)) # Finds the first element in cache
                self.cache.pop(LRUKey)

