class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairsCount = defaultdict(int)
        res = 0

        for n in nums:
            if pairsCount[k - n] > 0:
                res += 1
                pairsCount[k - n] -= 1
            else:
                pairsCount[n] += 1
        
        return res