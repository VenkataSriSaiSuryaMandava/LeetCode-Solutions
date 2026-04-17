class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.cap = capacity

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        prevNode.next = node
        nextNode.prev = node

        node.prev = prevNode
        node.next = nextNode
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.remove(self.map[key])

        self.map[key] = Node(key, value)
        self.insert(self.map[key])

        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)