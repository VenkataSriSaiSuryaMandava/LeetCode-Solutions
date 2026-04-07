class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.pos = []
        self.pos.append(((0, 0), "South"))

        for i in range(1, width):
            self.pos.append(((i, 0), "East"))
        
        for i in range(1, height):
            self.pos.append(((width - 1, i), "North"))
        
        for i in range(width - 2, -1, -1):
            self.pos.append(((i, height - 1), "West"))
        
        for i in range(height - 2, 0, -1):
            self.pos.append(((0, i), "South"))
        
        self.idx = 0
        self.isOrigin = True

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.isOrigin = False
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self):
        """
        :rtype: List[int]
        """
        return list(self.pos[self.idx][0])

    def getDir(self):
        """
        :rtype: str
        """
        if self.isOrigin:
            return "East"
        return self.pos[self.idx][1]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()