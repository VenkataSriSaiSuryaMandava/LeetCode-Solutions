class Solution:
    def maskPII(self, s: str) -> str:
        res = ""

        if s[0].isalpha():
            res += s[0].lower()
            res += "*****"

            i = 0
            while s[i + 1] != '@':
                i += 1
            res += s[i : ].lower()
            return res
        else:
            count = 0
            number = ""
            for ch in s:
                if '0' <= ch <= '9':
                    count += 1
                    number += ch

            res = '+' if count > 10 else ""
            localNumber = '***-***-' + number[-4 : ]

            if count > 10:
                res += '*' * (count - 10) + '-' + localNumber
                return res

            return localNumber