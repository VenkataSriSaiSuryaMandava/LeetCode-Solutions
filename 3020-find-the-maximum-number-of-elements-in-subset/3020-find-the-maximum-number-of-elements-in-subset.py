class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        res = count[1] - (count[1] % 2 ^ 1)
        del count[1]

        for num in count:
            length = 0

            while count[num] > 1:
                num = num * num
                length += 2
            
            length += 1 if count[num] else -1
            res = max(res, length)
        
        return res