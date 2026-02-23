class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0

        num1 = num1[ : : -1]
        num2 = num2[ : : -1]

        for i in range(max(len(num1), len(num2))):
            if i < len(num1):
                digit1 = ord(num1[i]) - ord('0')
            else:
                digit1 = 0
            
            if i < len(num2):
                digit2 = ord(num2[i]) - ord('0')
            else:
                digit2 = 0
            
            total = digit1 + digit2 + carry
            res = str(total % 10) + res
            carry = total // 10
        
        if carry:
            res = str(carry) + res
            
        return res