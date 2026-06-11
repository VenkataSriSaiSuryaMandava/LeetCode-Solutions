class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        dp = [envelopes[0][1]]

        for w, h in envelopes[1 : ]:
            if h > dp[-1]:
                dp.append(h)
            else:
                l = 0
                r = len(dp) - 1

                while l <= r:
                    m = (l + r) // 2

                    if h <= dp[m]:
                        r = m - 1
                    else:
                        l = m + 1
                
                dp[l] = h
        
        return len(dp)