class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHouses(l, r):
            rob1 = 0
            rob2 = 0

            for i in range(l, r + 1):
                temp = rob1
                rob1 = rob2
                rob2 = max(rob2, temp + nums[i])

            return rob2
        
        left = robHouses(0, len(nums) - 2)
        right = robHouses(1, len(nums) - 1)

        return max(left, right)