class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] > 0:
                nums[idx] = - nums[idx]
            
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res