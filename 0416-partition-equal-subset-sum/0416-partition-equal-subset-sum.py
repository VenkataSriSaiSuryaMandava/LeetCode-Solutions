class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for n in nums:
            nextDp = set()

            for t in dp:
                if n + t == target:
                    return True
                
                nextDp.add(t)
                nextDp.add(n + t)
            
            dp = nextDp
        
        return False