class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_ans = 0
        i = 0
        cur_sign = 1
        length = len(s)

        while i < length:
            if s[i].isdigit():
                number = 0
                digit_index = i

                while digit_index < length and s[digit_index].isdigit():
                    number = number * 10 + int(s[digit_index])
                    digit_index += 1

                cur_ans = cur_ans + cur_sign * number
                i = digit_index - 1
            
            elif s[i] == '+':
                cur_sign = 1
            
            elif s[i] == '-':
                cur_sign = -1
            
            elif s[i] == '(':
                stack.append(cur_ans)
                stack.append(cur_sign)

                cur_sign = 1
                cur_ans = 0

            elif s[i] == ')':
                prev_sign = stack.pop()
                prev_ans = stack.pop()

                cur_ans = prev_ans + prev_sign * cur_ans
        
            i += 1

        return cur_ans