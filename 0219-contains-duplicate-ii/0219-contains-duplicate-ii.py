class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i, n in enumerate(nums):
            if n in indices and abs(indices[n] - i) <= k:
                return True
            indices[n] = i
        return False