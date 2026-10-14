class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        
        count_9 = sum // 9
        rem = sum % 9
        
        if rem == 0:
            return "9" * count_9 + "0" * (num - count_9)
        else:
            return "9" * count_9 + str(rem) + "0" * (num - count_9 - 1)