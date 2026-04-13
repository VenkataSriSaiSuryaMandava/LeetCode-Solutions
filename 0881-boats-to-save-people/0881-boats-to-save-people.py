class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            remaining = limit - people[r]
            r -= 1
            res += 1

            if l <= r and remaining >= people[l]:
                l += 1

        return res  