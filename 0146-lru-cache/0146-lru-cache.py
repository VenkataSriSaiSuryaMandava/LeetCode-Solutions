class ListNode:
    def __init__(self, key=None, val=None):
        self.prev = None
        self.val = val
        self.next = None
        self.key = key

class LRUCache:
  
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = self.tail = ListNode()
        # self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.d:   return -1
        self.move_to_front(key)
        return self.d[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.get(key)
            self.d[key].val = value
        else:
            if len(self.d) == self.capacity:
                self.pop_left()
            self.add_node(key, value)
    
    def pop_left(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        del self.d[node.key]
    
    def add_node(self, key, value):
        node = ListNode(key, value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        
        self.d[key] = node
        

    def move_to_front(self, key):
        node = self.d[key]
        if node.next == self.tail:  return
        node.prev.next  = node.next
        node.next.prev = node.prev

        
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)