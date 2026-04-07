class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        cur_sign = 1
        cur_ans = 0

        i = 0
        length = len(s)
        digits = "0123456789"

        while i < length:
            if s[i] in digits:
                number = 0

                while i < length and s[i] in digits:
                    number = number * 10 + int(s[i])
                    i += 1

                i -= 1
                cur_ans = cur_ans + cur_sign * number

            elif s[i] == '+':
                cur_sign = 1
            
            elif s[i] == '-':
                cur_sign = -1
            
            elif s[i] == '(':
                stack.append(cur_ans)
                stack.append(cur_sign)

                cur_ans = 0
                cur_sign = 1
            
            elif s[i] == ')':
                prev_sign = stack.pop()
                prev_ans = stack.pop()

                cur_ans = prev_ans + prev_sign * cur_ans

            i += 1

        return cur_ans