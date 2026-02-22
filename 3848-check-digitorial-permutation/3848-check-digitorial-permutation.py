class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        digits = list(str(n))

        fact = [1] * 10
        for i in range(1, 10):
            fact[i] = fact[i - 1] * i

        max_possible = len(digits) * fact[9]
        if max_possible < n:
            return False
    
        seen = set()
        for p in permutations(digits):
            if p[0] == "0":
                continue

            num = int("".join(p))
            if num in seen:
                continue
            seen.add(num)

            s = 0
            for d in p:
                s += fact[int(d)]

            if num == s:
                return True

        return False