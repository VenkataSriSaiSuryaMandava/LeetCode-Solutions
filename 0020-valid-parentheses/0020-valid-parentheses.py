class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for ch in s:
            if ch in brackets:
                if not stack or stack.pop() != brackets[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack