class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0

        for num in range(num1, num2 + 1):
            num = str(num)

            for i in range(1, len(num) - 1):
                if num[i - 1] < num[i] > num[i + 1] or num[i - 1] > num[i] < num[i + 1]:
                    res += 1
        
        return res