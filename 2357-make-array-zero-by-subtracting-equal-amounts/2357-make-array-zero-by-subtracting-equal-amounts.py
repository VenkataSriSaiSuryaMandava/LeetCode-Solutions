class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen = set()

        for num in nums:
            if num > 0:
                seen.add(num)
        
        return len(seen)