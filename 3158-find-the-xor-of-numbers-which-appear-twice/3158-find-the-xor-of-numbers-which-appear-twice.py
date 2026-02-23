class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0

        for n in nums:
            count[n] += 1
        
        for key, val in count.items():
            if val == 2:
                res = res ^ key
        
        return res