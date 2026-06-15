class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prevIdx, prevTemp = stack.pop()
                res[prevIdx] = i - prevIdx
            
            stack.append([i, temp])
        
        return res