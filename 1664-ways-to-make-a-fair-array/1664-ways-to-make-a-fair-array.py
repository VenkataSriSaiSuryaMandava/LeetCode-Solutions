class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        s1 = sum(nums[ : : 2])
        s2 = sum(nums[1 : : 2])

        t1 = 0 
        t2 = 0
        res = 0

        for i, num in enumerate(nums):
            res += ((i % 2 == 0 and t2 + s1 - t1 - num == t1 + s2 - t2) or 
                    (i% 2 == 1 and t1 + s2 - t2 - num == t2 + s1 - t1))
            
            t1 += num if i % 2 == 0 else 0
            t2 += num if i % 2 == 1 else 0
        
        return res