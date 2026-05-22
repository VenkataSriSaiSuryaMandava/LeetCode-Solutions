class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a = a[ : : -1]
        b = b[: : -1]

        for i in range(max(len(a), len(b))):
            if i < len(a):
                digit1 = ord(a[i]) - ord('0')
            else:
                digit1 = 0
            
            if i < len(b):
                digit2 = ord(b[i]) - ord('0')
            else:
                digit2 = 0
            
            total = digit1 + digit2 + carry
            res = str(total % 2) + res
            carry = total // 2
        
        if carry:
            res = "1" + res
        
        return res