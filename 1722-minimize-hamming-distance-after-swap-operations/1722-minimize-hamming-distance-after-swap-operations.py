class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            
            return p[x]

        n = len(source)
        p = list(range(n))

        for a, b in allowedSwaps:
            p[find(a)] = find(b)
        
        count = defaultdict(Counter)
        res = 0

        for i, x in enumerate(source):
            j = find(i)
            count[j][x] += 1
        
        for i, x in enumerate(target):
            j = find(i)
            count[j][x] -= 1

            if count[j][x] < 0:
                res += 1

        return res