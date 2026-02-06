class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        res = 0
        
        for n in setnums:
            cur = n
            if cur - 1 not in setnums:
                count = 1
                cur += 1
                while cur in setnums:
                    count += 1
                    cur += 1
                res = max(count, res)
        return res