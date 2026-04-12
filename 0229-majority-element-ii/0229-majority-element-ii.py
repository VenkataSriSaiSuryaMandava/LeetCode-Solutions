class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) > 2:
                new_count = defaultdict(int)

                for num, cnt in count.items():
                    if cnt > 1:
                        new_count[num] = cnt - 1

                count = new_count
        
        res = []
        for num, cnt in count.items():
            if cnt > len(nums) // 3:
                res.append(num)
        
        return res