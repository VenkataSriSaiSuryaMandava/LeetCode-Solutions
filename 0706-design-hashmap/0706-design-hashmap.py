class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [LinkedList(0, 0) for i in range(10 ** 4)]

    def put(self, key: int, value: int) -> None:
        cur = self.hashmap[key % len(self.hashmap)]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            
            cur = cur.next
        
        cur.next = LinkedList(key, value)

    def get(self, key: int) -> int:
        cur = self.hashmap[key % len(self.hashmap)]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            
            cur = cur.next
        
        return -1

    def remove(self, key: int) -> None:
        cur = self.hashmap[key % len(self.hashmap)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)