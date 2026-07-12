class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}

        for i, num in enumerate(sorted(set(arr))):
            ranks[num] = i + 1

        return [ranks[num] for num in arr]