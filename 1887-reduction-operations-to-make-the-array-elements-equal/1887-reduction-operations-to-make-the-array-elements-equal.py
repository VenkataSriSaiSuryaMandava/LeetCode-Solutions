class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                count += 1
            
            res += count
        
        return res