class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        res = 0

        for i in range(len(nums)):
            largest = nums[i]
            smallest = nums[i]

            for j in range(i, len(nums)):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                res += largest - smallest
        
        return res