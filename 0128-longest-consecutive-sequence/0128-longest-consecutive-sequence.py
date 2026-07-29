class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for num in numsSet:
            count = 0

            if num - 1 not in numsSet:
                while num in numsSet:
                    num += 1
                    count += 1
                    res = max(count, res)
        
        return res