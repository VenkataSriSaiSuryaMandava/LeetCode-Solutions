class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for n in operations:
            if n == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif n == 'D':
                a = stack[-1]
                stack.append(a * 2)
            elif n == 'C':
                stack.pop()
            else:
                stack.append(int(n))
        
        return sum(stack)