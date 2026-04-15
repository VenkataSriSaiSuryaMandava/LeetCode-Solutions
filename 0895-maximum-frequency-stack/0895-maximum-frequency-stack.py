class FreqStack(object):

    def __init__(self):
        self.count = {}
        self.maxcnt = 0
        self.stacks = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        valCnt = 1 + self.count.get(val, 0)
        self.count[val] = valCnt

        if valCnt > self.maxcnt:
            self.maxcnt = valCnt
            self.stacks[self.maxcnt] = []
        
        self.stacks[valCnt].append(val)
        
    def pop(self):
        """
        :rtype: int
        """
        res = self.stacks[self.maxcnt].pop()

        self.count[res] -= 1

        if not self.stacks[self.maxcnt]:
            self.maxcnt -= 1
        
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()