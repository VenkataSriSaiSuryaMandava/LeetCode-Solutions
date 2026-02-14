class Solution:
    def fib(self, n: int) -> int:
        f1 = 0
        f2 = 1

        for i in range(n):
            temp = f1
            f1 = f1 + f2
            f2 = temp
        
        return f1
        