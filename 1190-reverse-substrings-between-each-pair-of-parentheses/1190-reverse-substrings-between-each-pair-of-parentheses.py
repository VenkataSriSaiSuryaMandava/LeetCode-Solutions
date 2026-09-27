class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                substr =  []

                while stack[-1] != '(':
                    substr.append(stack.pop())
                
                stack.pop()
                stack.extend(substr)
            else:
                stack.append(ch)
        
        return "".join(stack)