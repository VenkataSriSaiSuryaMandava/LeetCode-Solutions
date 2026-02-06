class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}
        
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next

        prevnode.next = nextnode
        nextnode.prev = prevnode

    def insert(self, node):
        prevnode = self.right.prev
        nextnode = self.right

        prevnode.next = node
        nextnode.prev = node

        node.prev = prevnode
        node.next = nextnode

    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        self.hash[key] = Node(key, value)
        self.insert(self.hash[key])

        if len(self.hash) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hash[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)