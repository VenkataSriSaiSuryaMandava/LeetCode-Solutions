class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.end = Node()
        self.head.next = self.end
        self.end.prev = self.head
        self.d = {}

    def add_node(self, key, val):
        node = Node(key, val)
        self.end.prev.next = node
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev = node
        return node

    def remove_node(self):
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next
        self.print()
        # if node.key in self.d:
        del self.d[node.key] 
        del node

    def move_to_end(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.d[node.key] = self.add_node(node.key, node.value)
        del node
        # self.print()

    def print(self):
        cur = self.head.next
        res = []
        while cur:
            res.append(str(cur.value))
            cur = cur.next
        # print('->'.join(res))

    def get(self, key: int) -> int:
        if key not in self.d:  return -1
        node = self.d[key]
        self.move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].value = value
            self.move_to_end(self.d[key])
            return
        
        if len(self.d) >= self.capacity:
            self.remove_node()
        node = self.add_node(key, value)
        self.d[key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)