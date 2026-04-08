class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        res = 0

        for l, r, k, v in queries:
            idx = l

            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        
        for num in nums:
            res ^= num
        
        return res