class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        res = 0

        for num in nums:
            while num:
                if num % 10 == digit:
                    res += 1
                num = num // 10

        return res