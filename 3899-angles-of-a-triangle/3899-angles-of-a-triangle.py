class Solution(object):
    def internalAngles(self, sides):
        """
        :type sides: List[int]
        :rtype: List[float]
        """
        a, b, c = sorted(sides)

        if a + b <= c or b + c <= a or c + a <= b:
            return []

        A = math.degrees(math.acos(float(b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        B = math.degrees(math.acos(float(a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        C = math.degrees(math.acos(float(a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))

        return sorted([A, B, C])