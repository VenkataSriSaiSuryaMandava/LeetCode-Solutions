class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        MOD = 10 ** 9 + 7
        res = 0

        for i in range(n):
            l = i
            r = n - 1

            while l <= r:
                m = (l + r) // 2

                if nums[i] + nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            
            if r >= i:
                res = (res + pow(2, r - i, MOD)) % MOD
        
        return res % MOD