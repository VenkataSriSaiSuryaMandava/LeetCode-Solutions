class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # I'll sort the candidates so I can prune larger values early.
        candidates.sort()

        # I'll store all valid combinations in this list.
        result = []

        # I'll track the current combination while exploring.
        path = []

        # I'll define a helper to explore candidates from a given index.
        def backtrack(start: int, remaining: int) -> None:

            # If I've reached the target, I'll save a copy of the path.
            if remaining == 0:
                result.append(path.copy())
                return

            # I'll only consider candidates at or after start.
            for i in range(start, len(candidates)):

                # I'll get the candidate I'm currently exploring.
                num = candidates[i]

                # If it's too large, I'll stop because the list is sorted.
                if num > remaining:
                    break

                # I'll include this candidate in the current combination.
                path.append(num)

                # I'll reuse index i because candidates can repeat.
                backtrack(i, remaining - num)

                # I'll undo my choice to explore other combinations.
                path.pop()

        # I'll begin with all candidates available and the full target.
        backtrack(0, target)

        # I'll return all the valid combinations I've collected.
        return result