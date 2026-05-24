class Solution:
    def passwordStrength(self, password: str) -> int:
        def points(ch):
            if ord('a') <= ord(ch) <= ord('z'):
                return 1
            elif ord('A') <= ord(ch) <= ord('Z'):
                return 2
            elif ch in "0123456789":
                return 3
            elif ch in "!@#$":
                return 5

        res = 0

        for ch in set(password):
            res += points(ch)

        return res