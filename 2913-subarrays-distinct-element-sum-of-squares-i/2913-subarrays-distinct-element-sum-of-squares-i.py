class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                res += count * count
        
        return res