class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            num = n

            while num:
                prod *= num % 10
                num = num // 10
            
            if prod % t == 0:
                return n
            
            n += 1