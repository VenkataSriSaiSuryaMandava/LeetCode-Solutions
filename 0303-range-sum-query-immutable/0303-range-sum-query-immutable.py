class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curSum = 0

        for n in nums:
            curSum += n
            self.prefix.append(curSum)

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix[left - 1] if left > 0 else 0
        rightSum = self.prefix[right]

        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)