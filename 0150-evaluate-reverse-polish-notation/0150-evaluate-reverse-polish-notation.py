class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    res = a + b
                elif i == '-':
                    res = b - a      
                elif i == '*':
                    res = b * a
                elif i == '/':
                    res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(i)) 
        return stack.pop()