class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k = sum(nums) % p
        if k == 0:
            return 0
        
        lastIdx = {0 : -1}
        cur = 0
        res = len(nums)

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - k + p) % p

            if target in lastIdx:
                res = min(res, i - lastIdx[target])
            
            lastIdx[cur] = i
        
        return res if res != len(nums) else -1
