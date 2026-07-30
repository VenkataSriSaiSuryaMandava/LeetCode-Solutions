class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0

        l = 0
        r = len(people) - 1

        while l <= r:
            rem = limit - people[r]
            r -= 1
            res += 1

            if l <= r and people[l] <= rem:
                l += 1
        
        return res