class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

            if len(count) > 2:
                newCount = defaultdict(int)

                for n, cnt in count.items():
                    if cnt > 1:
                        newCount[num] = cnt - 1
                
                count = newCount
        
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
