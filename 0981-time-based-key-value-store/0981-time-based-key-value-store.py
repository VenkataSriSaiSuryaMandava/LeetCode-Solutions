class TimeMap(object):

    def __init__(self):
        self.timestamp = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timestamp[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        cur = self.timestamp[key]

        l = 0
        r = len(cur) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if cur[m][1] <= timestamp:
                res = cur[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)