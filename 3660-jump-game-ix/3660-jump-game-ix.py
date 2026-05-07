class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        pre_max = [nums[0]] * n
        
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
            
        suf_min = float('inf')
        
        for i in range(n - 1, -1, -1):
            if i + 1 < n:
                ans[i] = ans[i + 1] if pre_max[i] > suf_min else pre_max[i]
            else:
                ans[i] = pre_max[i] if pre_max[i] <= suf_min else 0
            
            suf_min = min(suf_min, nums[i])
            
        return ans