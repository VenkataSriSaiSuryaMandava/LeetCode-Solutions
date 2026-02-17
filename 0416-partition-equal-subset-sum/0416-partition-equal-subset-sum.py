class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for n in nums:
            nextDP = set()

            for t in dp:
                if n + t == target:
                    return True
                nextDP.add(n + t)
                nextDP.add(t)
                
            dp = nextDP

        return False