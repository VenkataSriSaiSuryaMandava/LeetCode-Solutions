class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = rob1
            rob1 = rob2
            rob2 = max(rob2, n + temp)
        
        return rob2