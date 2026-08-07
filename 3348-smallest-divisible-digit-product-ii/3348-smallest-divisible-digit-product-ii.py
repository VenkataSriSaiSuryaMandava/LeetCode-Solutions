class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        c2 = c3 = c5 = c7 = 0
        while temp % 2 == 0:
            c2 += 1
            temp //= 2
        while temp % 3 == 0:
            c3 += 1
            temp //= 3
        while temp % 5 == 0:
            c5 += 1
            temp //= 5
        while temp % 7 == 0:
            c7 += 1
            temp //= 7
        if temp > 1:
            return "-1"

        def get_min_len(r2, r3, r5, r7):
            r2, r3, r5, r7 = max(0, r2), max(0, r3), max(0, r5), max(0, r7)
            d0 = (r2 + 2) // 3 + (r3 + 1) // 2
            d1 = 1 + (max(0, r2 - 1) + 2) // 3 + (max(0, r3 - 1) + 1) // 2
            return r5 + r7 + min(d0, d1)

        def consume(d, r2, r3, r5, r7):
            if d == 2: r2 -= 1
            elif d == 3: r3 -= 1
            elif d == 4: r2 -= 2
            elif d == 5: r5 -= 1
            elif d == 6: r2 -= 1; r3 -= 1
            elif d == 7: r7 -= 1
            elif d == 8: r2 -= 3
            elif d == 9: r3 -= 2
            return r2, r3, r5, r7

        n = len(num)
        zero_pos = num.find('0')

        if zero_pos == -1:
            cur2, cur3, cur5, cur7 = c2, c3, c5, c7
            for ch in num:
                cur2, cur3, cur5, cur7 = consume(int(ch), cur2, cur3, cur5, cur7)
            if cur2 <= 0 and cur3 <= 0 and cur5 <= 0 and cur7 <= 0:
                return num

        best_i = -1
        best_d = -1

        pref2, pref3, pref5, pref7 = c2, c3, c5, c7
        limit = zero_pos if zero_pos != -1 else n - 1

        for i in range(limit + 1):
            d_start = int(num[i]) + 1
            if d_start < 1:
                d_start = 1
            for d in range(d_start, 10):
                r2, r3, r5, r7 = consume(d, pref2, pref3, pref5, pref7)
                if get_min_len(r2, r3, r5, r7) <= n - 1 - i:
                    best_i = i
                    best_d = d
                    break
            if i == zero_pos:
                break
            pref2, pref3, pref5, pref7 = consume(int(num[i]), pref2, pref3, pref5, pref7)

        if best_i != -1:
            res = list(num[:best_i]) + [str(best_d)]
            r2, r3, r5, r7 = c2, c3, c5, c7
            for ch in res:
                r2, r3, r5, r7 = consume(int(ch), r2, r3, r5, r7)
            
            rem_len = n - len(res)
            for _ in range(rem_len):
                for d in range(1, 10):
                    nr2, nr3, nr5, nr7 = consume(d, r2, r3, r5, r7)
                    if get_min_len(nr2, nr3, nr5, nr7) <= rem_len - 1 - (len(res) - (best_i + 1)):
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        target_len = max(n + 1, get_min_len(c2, c3, c5, c7))
        res = []
        r2, r3, r5, r7 = c2, c3, c5, c7
        for i in range(target_len):
            rem = target_len - 1 - i
            for d in range(1, 10):
                nr2, nr3, nr5, nr7 = consume(d, r2, r3, r5, r7)
                if get_min_len(nr2, nr3, nr5, nr7) <= rem:
                    res.append(str(d))
                    r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                    break
        return "".join(res)