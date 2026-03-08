class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)

        for n in arr:
            count[n] += 1
        
        return len(count) == len(set(count.values()))