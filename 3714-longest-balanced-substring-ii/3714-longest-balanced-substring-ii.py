class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 1

        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)

        pairs = [('a', 'b'), ('a', 'c'), ('b', 'c')]

        for x, y in pairs:
            diff_index = {0: -1}
            diff = 0

            for i, ch in enumerate(s):
                if ch == x:
                    diff += 1
                elif ch == y:
                    diff -= 1
                else:
                    diff = 0
                    diff_index = {0: i}
                    continue

                if diff in diff_index:
                    ans = max(ans, i - diff_index[diff])
                else:
                    diff_index[diff] = i

        a = b = c = 0
        seen = {(0, 0): -1}

        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            key = (b - a, c - a)

            if key in seen:
                ans = max(ans, i - seen[key])
            else:
                seen[key] = i

        return ans