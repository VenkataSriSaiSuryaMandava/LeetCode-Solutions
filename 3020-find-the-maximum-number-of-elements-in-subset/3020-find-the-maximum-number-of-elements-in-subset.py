class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        res = count[1] - (count[1] % 2 ^ 1)
        del count[1]

        for num in count:
            length = 0
            cur_num = num

            while count[cur_num] > 1:
                cur_num = cur_num * cur_num
                length += 2
            
            length += 1 if count[cur_num] else -1
            res = max(res, length)
        
        return res