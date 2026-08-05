class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1] [1] < temp:
                idx, t = stack.pop()
                res[idx] = i - idx
            
            stack.append([i, temp])
        
        return res