class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visit = defaultdict(int)

        for n in nums:
            visit[n] += 1
        
        for key, val in visit.items():
            if val == 1:
                return key