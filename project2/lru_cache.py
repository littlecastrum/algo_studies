from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, max_length=100000):
        assert max_length > 0
        self.cache = OrderedDict()
        self.max_length = max_length

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.max_length:
            self.cache.popitem(last=False)

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def __repr__(self):
        return str(self.cache)

def main():
    cache = LRU_Cache(5)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(9))
    cache.set(5, 5) 
    cache.set(6, 6)
    print(cache.get(3))
    print(cache)

if __name__ == '__main__':
    main()