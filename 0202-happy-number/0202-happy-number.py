class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            res = 0
            while n:
                digit = n % 10
                n = n // 10
                res += digit ** 2
            n = res
        return n == 1