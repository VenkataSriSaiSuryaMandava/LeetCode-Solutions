class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        get_val = self.timemap[key]
        l = 0
        r = len(get_val) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if get_val[m][1] <= timestamp:
                res = get_val[m][0]
                l = m + 1
            elif get_val[m][1] > timestamp:
                r = m - 1
        
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)