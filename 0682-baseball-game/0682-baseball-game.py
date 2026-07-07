class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ch in operations:
            if ch == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif ch == 'D':
                a = stack[-1]
                stack.append(a * 2)
            elif ch == 'C':
                stack.pop()
            else:
                stack.append(int(ch))
        
        return sum(stack)