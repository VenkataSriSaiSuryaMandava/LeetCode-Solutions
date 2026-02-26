class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        res = []
        for num, cnt in count.items():
            if cnt > len(nums) // 3:
                res.append(num)
            
        return res