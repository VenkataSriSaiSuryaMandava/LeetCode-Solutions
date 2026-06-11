class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        setNums = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in setNums:
                res.append(i)
        
        return res