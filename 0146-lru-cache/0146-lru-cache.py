class Node:
    def __init__(self, key:int, val:int):
        self.key, self.val = key, val
        self.next, self.prev = None, None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node) -> None:
        # remove from cache and linked list
        del self.cache[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert(self, node) -> None:
        # insert to cache and linked list
        self.cache[node.key] = node
        mru = self.right.prev
        mru.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = mru

    def get(self, key: int) -> int:
        if key in self.cache:
            # 1. update linked list
            key, val = self.cache[key].key, self.cache[key].val
            self.remove(self.cache[key])
            self.insert(Node(key,val))
            # 2. return val
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # 1. insert new node
        self.insert(Node(key, value))
        # 2. if over capacity -> delete
        if len(self.cache.keys()) > self.cap:
            lru = self.left.next
            self.remove(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)