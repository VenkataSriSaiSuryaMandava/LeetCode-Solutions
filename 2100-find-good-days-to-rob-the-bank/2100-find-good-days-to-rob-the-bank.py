class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        res = []

        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        
        for i in range(n):
            if left[i] >= time and right[i] >= time:
                res.append(i)
        
        return res