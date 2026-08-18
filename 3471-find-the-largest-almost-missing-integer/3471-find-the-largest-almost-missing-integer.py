class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = -1

        for i in range(len(nums) - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])
            
            for num in seen:
                count[num] += 1
        
        for num, cnt in count.items():
            if cnt == 1:
                res = max(res, num)
        
        return res