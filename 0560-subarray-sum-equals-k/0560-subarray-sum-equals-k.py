class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0 : 1}
        res = 0
        prefix = 0

        for num in nums:
            prefix += num
            diff = prefix - k
            
            res += count.get(diff, 0)
            count[prefix] = 1 + count.get(prefix, 0)
        
        return res
