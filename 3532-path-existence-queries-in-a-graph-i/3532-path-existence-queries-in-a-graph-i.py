class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        groups = [0]
        count = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                count += 1
            
            groups.append(count)
        
        return [groups[u] == groups[v] for u, v in queries]