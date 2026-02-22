class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.SumofSquares(n)

        while slow != fast:
            fast = self.SumofSquares(fast)
            fast = self.SumofSquares(fast)
            slow = self.SumofSquares(slow)
        
        if fast == 1:
            return True
        else:
            return False

    def SumofSquares(self, n):
        res = 0

        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        
        return res