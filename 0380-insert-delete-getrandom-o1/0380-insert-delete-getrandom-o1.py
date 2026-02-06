class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.array)
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            idx = self.map[val]
            last_value = self.array[-1]
            self.array[idx] = last_value
            self.array.pop()
            self.map[last_value] = idx
            del self.map[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()