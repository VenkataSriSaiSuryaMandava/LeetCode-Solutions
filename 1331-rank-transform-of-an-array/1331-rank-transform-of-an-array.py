class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = arr.copy()
        nums.sort()

        ranks = {}
        rank = 1

        for num in nums:
            if num not in ranks:
                ranks[num] = rank
                rank += 1

        return [ranks[num] for num in arr]