class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif op == "D":
                a = stack[-1]
                stack.append(a * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)