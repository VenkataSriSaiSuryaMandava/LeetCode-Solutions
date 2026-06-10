class Solution:

    def __init__(self, w: List[int]):
        self.range = -1
        self.ranges = []

        for weight in w:
            self.range += weight
            self.ranges.append(self.range)

    def pickIndex(self) -> int:
        randomNum = random.randint(0, self.range)

        l = 0
        r = len(self.ranges) - 1

        while l <= r:
            m = (l + r) // 2

            if randomNum > self.ranges[m]:
                l = m + 1
            else:
                r = m - 1
        
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()