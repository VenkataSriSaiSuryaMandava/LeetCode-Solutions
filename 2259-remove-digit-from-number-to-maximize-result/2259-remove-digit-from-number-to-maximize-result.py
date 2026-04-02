class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        res = ""
        for i in range(len(number)):
            if number[i] == digit:
                cur = number[ : i] + number[i + 1 : ]
                if cur > res:
                    res = cur
        
        return res
        