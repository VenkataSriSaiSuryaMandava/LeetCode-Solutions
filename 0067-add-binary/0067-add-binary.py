class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a = a[ : : -1]
        b = b[ : : -1]

        for i in range(max(len(a), len(b))):
            if i < len(a):
                digitA = ord(a[i]) - ord("0")
            else:
                digitA = 0
            
            if i < len(b):
                digitB = ord(b[i]) - ord("0")
            else:
                digitB = 0
            
            total = digitA + digitB + carry
            res = str(total % 2) + res
            carry = total // 2
        
        if carry:
            res = "1" + res

        return res