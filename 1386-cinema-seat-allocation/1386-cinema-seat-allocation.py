class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved = defaultdict(set)
        res = 0

        for row, seat in reservedSeats:
            reserved[row].add(seat)
        
        for row, seats in reserved.items():
            left = all(s not in seats for s in [2, 3, 4, 5])
            middle = all(s not in seats for s in [4, 5, 6, 7])
            right = all(s not in seats for s in [6, 7, 8, 9])

            if left and right:
                res += 2
            elif left or right or middle:
                res += 1
        
        res += 2 * (n - len(reserved))

        return res