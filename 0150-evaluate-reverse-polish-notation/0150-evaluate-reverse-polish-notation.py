class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for n in tokens:
            if n in "+-*/":
                a = stack.pop()
                b = stack.pop()

                if n == "+":
                    stack.append(a + b)
                elif n == "-":
                    stack.append(b - a)
                elif n == "*":
                    stack.append(a * b)
                elif n == '/':
                    stack.append(int(float(b) / a))

            else:
                stack.append(int(n))
        
        return stack.pop()