class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)

        for i in range(len(nums) - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            
            for n in seen:
                count[n] += 1

        res = -1
        for num, val in count.items():
            if val == 1:
                res = max(res, num)
        
        return res