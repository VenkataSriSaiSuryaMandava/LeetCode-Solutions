class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        node.next = nextNode
        node.prev = prevNode

        nextNode.prev = node
        prevNode.next = node

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.right.prev.val
        
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