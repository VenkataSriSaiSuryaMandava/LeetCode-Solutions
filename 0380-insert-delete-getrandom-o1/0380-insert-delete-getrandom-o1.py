class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        
        self.map[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        
        idx = self.map[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.arr.pop()

        self.map[last] = idx
        del self.map[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()