class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.removed = set()

    def popSmallest(self) -> int:
        small = self.smallest
        self.removed.add(small)
        
        while self.smallest in self.removed:
            self.smallest += 1
        
        return small

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            if num < self.smallest:
                self.smallest = num
            

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)