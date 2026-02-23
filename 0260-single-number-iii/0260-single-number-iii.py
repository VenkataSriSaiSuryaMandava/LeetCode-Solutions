class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor = xor ^ n
        
        diff_bit = 1
        while not(diff_bit & xor):
            diff_bit = diff_bit << 1
        
        a = 0
        b = 0

        for n in nums:
            if diff_bit & n:
                a = a ^ n
            else:
                b = b ^ n
        
        return [a, b]