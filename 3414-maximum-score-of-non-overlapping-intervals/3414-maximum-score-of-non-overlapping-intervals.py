from bisect import bisect_left
from typing import List


class Solution:

  def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    events = sorted(
        [(iv[0], iv[1], iv[2], i) for i, iv in enumerate(intervals)],
        key=lambda x: x[1],
    )
    ends = [iv[1] for iv in events]

    dp = [[(0, ())] * 5 for _ in range(n + 1)]

    def is_better(cand, current):
      if cand[0] != current[0]:
        return cand[0] > current[0]
      return cand[1] < current[1]

    for i in range(n):
      l, r, w, orig_idx = events[i]
      j = bisect_left(ends, l)

      for c in range(1, 5):
        best = dp[i][c]
        prev_weight, prev_indices = dp[j][c - 1]

        if c == 1 or prev_weight > 0 or prev_indices:
          new_weight = prev_weight + w
          new_indices = tuple(sorted(prev_indices + (orig_idx,)))
          candidate = (new_weight, new_indices)

          if is_better(candidate, best):
            best = candidate

        dp[i + 1][c] = best

    best_overall = (0, ())
    for c in range(1, 5):
      if is_better(dp[n][c], best_overall):
        best_overall = dp[n][c]

    return list(best_overall[1])