class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                poptemp, popindex = stack.pop()
                answer[popindex] = i - popindex 
            stack.append((temp, i))
        
        return answer