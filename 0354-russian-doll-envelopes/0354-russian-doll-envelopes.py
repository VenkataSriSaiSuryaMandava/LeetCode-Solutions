class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        dp = [envelopes[0][1]]

        for w, h in envelopes[1 : ]:
            if h > dp[-1]:
                dp.append(h)
            else:
                idx = bisect_left(dp, h)
                dp[idx] = h
        
        return len(dp)