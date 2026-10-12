class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIdx = {}

        for i, num in enumerate(nums):
            if target - num in numToIdx:
                return [i, numToIdx[target - num]]
            
            numToIdx[num] = i