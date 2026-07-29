class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            diff = prefix - k

            res += count.get(diff, 0)
            count[prefix] = 1 + count.get(prefix, 0)
        
        return res