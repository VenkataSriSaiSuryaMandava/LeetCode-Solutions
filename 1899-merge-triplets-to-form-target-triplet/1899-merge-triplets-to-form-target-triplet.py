class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        tripletSet = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    tripletSet.add(i)
        
        return len(tripletSet) == 3