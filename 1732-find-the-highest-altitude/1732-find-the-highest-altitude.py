class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        altitude = 0

        for netgain in gain:
            altitude += netgain
            res = max(res, altitude)
        
        return res