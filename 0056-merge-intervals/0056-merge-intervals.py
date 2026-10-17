class Solution:

    # I'll create a method that takes the intervals and returns the merged result.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # I'll handle an empty input right away.
        if not intervals:

            # I'll return an empty list because there are no intervals to merge.
            return []

        # I'll sort the intervals by their starting values.
        intervals.sort(key=lambda interval: interval[0])

        # I'll initialize the result with the first interval.
        merged = [intervals[0][:]]

        # I'll go through the remaining intervals one by one.
        for start, end in intervals[1:]:

            # I'll check whether the current interval overlaps with the last merged interval.
            if start <= merged[-1][1]:

                # I'll extend the end only if the current interval goes further.
                merged[-1][1] = max(merged[-1][1], end)

            # Otherwise, the current interval doesn't overlap.
            else:

                # I'll add it as a separate interval.
                merged.append([start, end])

        # I'll return the final list of non-overlapping intervals.
        return merged