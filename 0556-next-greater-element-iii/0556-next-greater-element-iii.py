class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        length = len(digits)

        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i < 0:
            return -1
        
        j = length - 1
        while digits[i] >= digits[j]:
            j -= 1
        
        digits[i], digits[j] = digits[j], digits[i]

        l = i + 1
        r = length - 1

        while l < r:
            digits[l], digits[r] = digits[r], digits[l]
            l += 1
            r -= 1
        
        res = int("".join(digits))

        if res > 2 ** 31 - 1:
            return -1
        else:
            return res