from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_remove = right_remove = 0

        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, left, right, balance, path):
            if balance < 0:
                return

            if index == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.add("".join(path))
                return

            char = s[index]

            if char == '(' and left > 0:
                backtrack(index + 1, left - 1, right, balance, path)

            if char == ')' and right > 0:
                backtrack(index + 1, left, right - 1, balance, path)

            path.append(char)

            if char == '(':
                backtrack(index + 1, left, right, balance + 1, path)
            elif char == ')':
                backtrack(index + 1, left, right, balance - 1, path)
            else:
                backtrack(index + 1, left, right, balance, path)

            path.pop()

        backtrack(0, left_remove, right_remove, 0, [])

        return list(result)