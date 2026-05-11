class Node:
    def __init__(self, key, val=0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right #lru
        self.right.prev = self.left #mru
    
    def remove(self, node):
        node.prev.next = node.next if node.next else None
        node.next.prev = node.prev  if node.prev else None

        return

    def insert(self, node):
        mru = self.right.prev
        mru.next = node
        node.prev = mru
        self.right.prev = node
        node.next = self.right

        return

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
        else: 
            new_node = Node(key , value)
            self.insert(new_node)
            self.cache[key] = new_node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        return

# Test 1: Basic usage
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # evicts key 2 (LRU)
print(cache.get(2))    # -1

# Test 2: Update refreshes recency
cache2 = LRUCache(2)
cache2.put(1, 10)
cache2.put(2, 20)
cache2.put(1, 100)     # update — key 1 is now MRU
cache2.put(3, 30)      # evicts key 2
print(cache2.get(1))   # 100
print(cache2.get(2))   # -1

# Test 3: get() refreshes recency
cache3 = LRUCache(2)
cache3.put(1, 1)
cache3.put(2, 2)
cache3.get(1)          # key 1 is now MRU
cache3.put(3, 3)       # evicts key 2
print(cache3.get(1))   # 1
print(cache3.get(2))   # -1

# Test 4: capacity 1
cache4 = LRUCache(1)
cache4.put(1, 1)
cache4.put(2, 2)       # evicts key 1
print(cache4.get(1))   # -1
print(cache4.get(2))   # 2

# Test 5: overwrite existing key, no eviction
cache5 = LRUCache(2)
cache5.put(1, 1)
cache5.put(1, 42)      # update, no eviction
cache5.put(2, 2)
print(cache5.get(1))   # 42