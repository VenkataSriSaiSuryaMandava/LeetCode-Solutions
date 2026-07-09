class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"

        num1 = num1[ : : -1]
        num2 = num2[ : : -1]

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                digit = digit1 * digit2

                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        beg = 0
        res = res[ : : -1]

        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        return "".join(map(str, res[beg : ]))