class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digit = carry + digits[i]
            digits[i] = digit % 10
            carry = digit // 10

        if carry:
            digits.insert(0, carry)
            
        return digits