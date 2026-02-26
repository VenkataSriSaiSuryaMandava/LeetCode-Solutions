class Solution:
    def numSteps(self, s: str) -> int:
        res = 0 
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            digit = (int(s[i]) + carry) % 2

            if digit:
                res += 2
                carry = 1
            else:
                res += 1
        
        return res + carry