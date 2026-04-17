class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.space = k
        self.left = Node(0, None, None)
        self.right = Node(0, self.left, None)
        self.left.next = self.right

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        cur = Node(value, self.right.prev, self.right)
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1

        return True
        
    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1

        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.left.next.val

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.right.prev.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.left.next == self.right

    def isFull(self):
        """
        :rtype: bool
        """
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()