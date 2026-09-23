class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        sumToIndex = {0 : -1}
        maxLength = -1
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            sumToIndex[prefix] = i

            if prefix - target in sumToIndex:
                maxLength = max(maxLength, i - sumToIndex[prefix - target])
        
        return -1 if maxLength == -1 else len(nums) - maxLength