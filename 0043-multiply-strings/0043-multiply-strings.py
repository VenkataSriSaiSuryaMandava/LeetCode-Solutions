class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1 = num1[ : : -1]
        num2 = num2[ : : -1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                digit = digit1 * digit2

                res[i + j] += digit
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = res[i + j] % 10
        
        res = res[ : : -1]
        beg = 0

        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        res = map(str, res[beg : ])

        return "".join(res)