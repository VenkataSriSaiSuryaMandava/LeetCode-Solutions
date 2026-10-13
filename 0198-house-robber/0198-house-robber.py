class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = rob1
            rob1 = rob2
            rob2 = max(rob2, num + temp)
        
        return rob2